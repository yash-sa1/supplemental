"""
Task 01 · Core · Build a Hash Map (separate chaining)  (SOLUTION)

    buckets[0] -> []
    buckets[1] -> [["cat", 1], ["act", 7]]    <- collision: same bucket, chained
    buckets[2] -> [["dog", 4]]
    ...
"""
from collections.abc import Hashable, Iterator
from typing import Any


class HashMap:
    INITIAL_CAPACITY = 8
    MAX_LOAD_FACTOR = 0.75

    def __init__(self):
        self.capacity = self.INITIAL_CAPACITY
        self._buckets: list[list[list]] = [[] for _ in range(self.capacity)]
        self._size = 0

    def _bucket(self, key: Hashable) -> list[list]:
        return self._buckets[hash(key) % self.capacity]

    def _resize(self, new_capacity: int) -> None:
        old = self._buckets
        self.capacity = new_capacity
        self._buckets = [[] for _ in range(new_capacity)]
        for bucket in old:
            for key, value in bucket:
                # the bucket index depends on capacity, so every entry moves
                self._bucket(key).append([key, value])

    def __setitem__(self, key: Hashable, value: Any) -> None:
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value  # overwrite: size unchanged
                return
        bucket.append([key, value])
        self._size += 1
        if self._size > self.MAX_LOAD_FACTOR * self.capacity:
            self._resize(self.capacity * 2)

    def __getitem__(self, key: Hashable) -> Any:
        for k, v in self._bucket(key):
            if k == key:
                return v
        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)  # chains are short, so this is O(1) on average
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key: Hashable) -> bool:
        return any(k == key for k, _ in self._bucket(key))

    def get(self, key: Hashable, default: Any = None) -> Any:
        try:
            return self[key]
        except KeyError:
            return default

    def __len__(self) -> int:
        return self._size

    def items(self) -> list[tuple]:
        return [(k, v) for bucket in self._buckets for k, v in bucket]

    def keys(self) -> list:
        return [k for k, _ in self.items()]

    def values(self) -> list:
        return [v for _, v in self.items()]

    def __iter__(self) -> Iterator:
        return iter(self.keys())
