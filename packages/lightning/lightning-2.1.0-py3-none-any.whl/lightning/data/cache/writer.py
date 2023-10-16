# Copyright The Lightning AI team.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
from time import sleep
from typing import Any, Dict, List, Optional

import numpy as np

from lightning.data.cache.compression import _COMPRESSORS, Compressor
from lightning.data.cache.constants import _INDEX_FILENAME, _TORCH_2_1_0_AVAILABLE
from lightning.data.cache.serializers import _SERIALIZERS, Serializer
from lightning.data.datasets.env import _DistributedEnv, _WorkerEnv

if _TORCH_2_1_0_AVAILABLE:
    from torch.utils._pytree import PyTree, tree_flatten, treespec_dumps


class BinaryWriter:
    def __init__(
        self,
        cache_dir: str,
        chunk_size: Optional[int] = None,
        chunk_bytes: Optional[int] = None,
        compression: Optional[str] = None,
    ):
        """The BinaryWriter enables to chunk dataset into an efficient streaming format for cloud training.

        Arguments:
            cache_dir: The path to where the chunks will be saved.
            chunk_bytes: The maximum number of bytes within a chunk.
            chunk_size: The maximum number of items within a chunk.
            compression: The compression algorithm to use.

        """
        self._cache_dir = cache_dir

        if not os.path.exists(self._cache_dir):
            raise FileNotFoundError(f"The provided cache directory `{self._cache_dir}` doesn't exist.")

        if (chunk_size is None and chunk_bytes is None) or (chunk_size and chunk_bytes):
            raise ValueError("Either one of the `chunk_size` or the `chunk_bytes` need to be provided.")

        self._serializers: Dict[str, Serializer] = _SERIALIZERS
        self._chunk_size = chunk_size
        self._chunk_bytes = chunk_bytes
        self._compression = compression

        self._data_format: Optional[List[str]] = None
        self._data_spec: Optional[PyTree] = None

        if self._compression:
            if len(_COMPRESSORS) == 0:
                raise ValueError("No compresion algorithms are installed.")
            if self._compression not in _COMPRESSORS:
                raise ValueError(
                    f"The provided compression {self._compression} isn't available in {sorted(_COMPRESSORS)}"
                )
            self._compressor: Compressor = _COMPRESSORS[self._compression]

        self._current_chunk_bytes = 0
        self._chunk_index = 0
        self._serialized_items: List[bytes] = []
        self._chunks_info: List[Dict[str, Any]] = []
        self._indexes: List[int] = []
        self._worker_env: Optional[_WorkerEnv] = None
        self._rank: Optional[int] = None
        self._is_done = False
        self._distributed_env = _DistributedEnv.detect()

    @property
    def filled(self) -> bool:
        """Returns whether the caching phase is done."""
        if self._is_done:
            return True
        files = os.listdir(self._cache_dir)
        index_files = [f for f in files if f.endswith(_INDEX_FILENAME)]
        worker_end = _WorkerEnv.detect()
        self._is_done = len(index_files) == self._distributed_env.world_size * worker_end.world_size
        return self._is_done

    @property
    def rank(self) -> int:
        """Returns the rank of the writer."""
        if self._rank is None:
            self._worker_env = _WorkerEnv.detect()
            self._rank = self._distributed_env.global_rank * self._worker_env.world_size + self._worker_env.rank
        return self._rank

    def get_config(self) -> Dict[str, Any]:
        """Returns the config of the writer."""
        out = {
            "compression": self._compression,
            "chunk_size": self._chunk_size,
            "chunk_bytes": self._chunk_bytes,
            "data_format": self._data_format,
            "data_spec": treespec_dumps(self._data_spec) if self._data_spec else None,
        }
        return out

    def serialize(self, items: Any) -> bytes:
        """Serialize a dictionary into its binary format."""

        # Flatten the items provided by the users
        flattened, data_spec = tree_flatten(items)

        # Collect the sizes and associated bytes for each item
        sizes: List[int] = []
        data: List[bytes] = []

        data_format: List[str] = []
        for item in flattened:
            data_format.append(self._serialize(item, sizes, data))

        if self._data_format is None:
            self._data_format = data_format
        elif self._data_format != data_format:
            raise Exception(
                f"The data format changed between items. Found {data_format} instead of {self._data_format}."
            )

        if self._data_spec is None:
            self._data_spec = data_spec
        elif self._data_spec != data_spec:
            raise Exception(f"The data format changed between items. Found {data_spec} instead of {self._data_spec}.")

        # Concatenante into a single byte array
        head = np.array(sizes, np.uint32).tobytes()
        body = b"".join(data)
        return head + body

    def _serialize(self, item: Any, sizes: List[int], data: List[bytes]) -> str:
        """Serialize a given item and append its size and bytes to the sizes and data array."""
        for serializer_name, serializer in self._serializers.items():
            if serializer.can_serialize(item):
                serialized_item, name = serializer.serialize(item)
                data.append(serialized_item)
                sizes.append(len(serialized_item))
                return name or serializer_name
        raise ValueError(f"The provided item isn't serializable. Found {item}")

    def _create_chunk(self, filename: str) -> bytes:
        """Create a binary chunk from all the binarized items."""
        num_items = np.uint32(len(self._serialized_items))
        sizes = list(map(len, self._serialized_items))
        offsets = np.array([0] + sizes).cumsum().astype(np.uint32)
        offsets += len(num_items.tobytes()) + len(offsets.tobytes())
        sample_data = b"".join(self._serialized_items)
        data = num_items.tobytes() + offsets.tobytes() + sample_data
        offsets = offsets.tolist()
        mapping = {}
        for i in range(len(self._indexes)):
            mapping[self._indexes[i]] = [offsets[i], offsets[i + 1]]

        assert len(mapping) == len(self._indexes)
        assert (self._indexes[-1] - self._indexes[0] + 1) == len(self._serialized_items)

        chunk_info = {
            "chunk_bytes": self._current_chunk_bytes,
            "chunk_size": len(self._serialized_items),
            "filename": filename,
            "interval": [self._indexes[0], self._indexes[-1] + 1],
        }

        self._chunks_info.append(chunk_info)

        return data

    def write_chunk(self) -> None:
        """Write a chunk to the filesystem."""
        if self._compression:
            filename = f"chunk-{self.rank}-{self._chunk_index}.{self._compression}.bin"
        else:
            filename = f"chunk-{self.rank}-{self._chunk_index}.bin"
        self.write_chunk_to_file(self._create_chunk(filename), filename)

    def reset(self) -> None:
        """Reset the writer to handle the next chunk."""
        self._serialized_items = []
        self._indexes = []
        self._current_chunk_bytes = 0

    def __setitem__(self, index: int, items: Any) -> None:
        """Store an item to a chunk.

        The index needs to be provided in order.

        This is handled by the samplers automatically. This ensures we can map an index to a shard from an interval.

        """
        # Serialize the items
        serialized_items = self.serialize(items)
        serialized_items_size = len(serialized_items)

        # Check whether it is time to write a chunk
        should_write = (
            self._chunk_bytes and self._chunk_bytes < self._current_chunk_bytes + serialized_items_size
        ) or (self._chunk_size and len(self._indexes) >= self._chunk_size)

        if should_write:
            if self._current_chunk_bytes == 0:
                raise Exception(
                    f"The provided chunk_size {self._chunk_bytes} is too small."
                    f" You should use a multiple of {serialized_items_size} bytes."
                )
            self.write_chunk()
            self.reset()
            self._chunk_index += 1

        # Store the serialized items into the chunk.
        self._serialized_items.append(serialized_items)
        self._current_chunk_bytes += serialized_items_size

        # Validate the index are provided in an incremental order
        # This is required to ensure we can find efficiently a chunk index from an index using the chunk interval
        if self._indexes:
            assert self._indexes[-1] == index - 1, (self._indexes, index - 1)

        # Store the index
        self._indexes.append(index)

    def write_chunk_to_file(
        self,
        raw_data: bytes,
        filename: str,
    ) -> None:
        """Write chunk bytes to a file."""
        # Whether to compress the raw bytes
        if self._compression:
            raw_data = self._compressor.compress(raw_data)

        # Write the binary chunk file
        with open(os.path.join(self._cache_dir, filename), "wb") as out:
            out.write(raw_data)

    def write_chunks_index(self) -> None:
        """Write the chunks index to a JSON file."""
        filepath = os.path.join(self._cache_dir, f"{self.rank}.{_INDEX_FILENAME}")
        config = self.get_config()
        with open(filepath, "w") as out:
            json.dump({"chunks": self._chunks_info, "config": config}, out, sort_keys=True)

    def done(self) -> None:
        """Called when StopIteration is triggered."""
        if self.filled:
            return
        if self._serialized_items:
            self.write_chunk()
        self.write_chunks_index()
        self.reset()
        self._is_done = True

    def merge(self, num_workers: int = 1) -> None:
        """Once all the workers have written their own index, the merge function is responsible to read and merge them
        into a single index."""
        num_workers = num_workers or 1

        # Only for non rank 0
        if self.rank != 0:
            while not os.path.exists(os.path.join(self._cache_dir, _INDEX_FILENAME)):
                sleep(0.001)
            return

        # Wait for all indexes to be available
        is_done = False
        while not is_done:
            files = os.listdir(self._cache_dir)
            if _INDEX_FILENAME in files:
                return
            index_files = [f for f in files if f.endswith(_INDEX_FILENAME)]
            is_done = len(index_files) == self._distributed_env.world_size * num_workers
            sleep(0.001)

        # Read the index and append the chunks together
        chunks_info = []
        config = None
        for index_filename in sorted(index_files):
            chunk_path = os.path.join(self._cache_dir, index_filename)
            with open(chunk_path) as f:
                data = json.load(f)

                if config is None:
                    config = data["config"]

                elif config != data["config"]:
                    raise Exception("The config isn't consistent between chunks. This shouldn't have happened.")

                chunks_info.extend(data["chunks"])

            os.remove(chunk_path)

        # Write down the collected index
        with open(os.path.join(self._cache_dir, _INDEX_FILENAME), "w") as f:
            json.dump({"chunks": chunks_info, "config": config}, f, sort_keys=True)
