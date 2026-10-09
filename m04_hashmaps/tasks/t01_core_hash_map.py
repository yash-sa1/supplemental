"""
Task 01 · Core · Build a Hash Map (separate chaining)

Implement a dictionary from scratch WITHOUT using dict or set anywhere
inside it. Storage is a Python list of buckets; each bucket is a list of
[key, value] pairs (separate chaining handles collisions).

Rules the tests rely on:
    - self.capacity  = current number of buckets. Starts at 8.
    - Bucket for a key: hash(key) % self.capacity
    - After an insert that adds a NEW key, if len(self) > 0.75 * capacity
      (the load factor limit), double the capacity and re-hash every entry
      into the new buckets. (So with capacity 8 the 7th key triggers a resize to 16.)
    - Overwriting an existing key never changes len() or triggers a resize.
    - Keys are compared with ==  (so 1 and 1.0 are the same key, like dict).

Required behaviour (average case):
    m[key] = value       O(1)  insert or overwrite
    m[key]               O(1)  raise KeyError if missing
    del m[key]           O(1)  raise KeyError if missing
    key in m             O(1)
    m.get(key, default)  O(1)  default is None if not given
    len(m)               O(1)
    m.keys() / m.values() / m.items()   -> lists, any order
    for k in m           iterate over keys

Example:
    m = HashMap()
    m["apple"] = 3
    m["apple"] = 5          # overwrite
    m["apple"]      -> 5
    "pear" in m     -> False
    m.get("pear", 0) -> 0
    len(m)          -> 1
"""
from collections.abc import Hashable, Iterator
from typing import Any


class HashMap:
    INITIAL_CAPACITY = 8
    MAX_LOAD_FACTOR = 0.75

    def __init__(self):
        raise NotImplementedError

    def __setitem__(self, key: Hashable, value: Any) -> None:
        raise NotImplementedError

    def __getitem__(self, key: Hashable) -> Any:
        raise NotImplementedError

    def __delitem__(self, key: Hashable) -> None:
        raise NotImplementedError

    def __contains__(self, key: Hashable) -> bool:
        raise NotImplementedError

    def get(self, key: Hashable, default: Any = None) -> Any:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def keys(self) -> list:
        raise NotImplementedError

    def values(self) -> list:
        raise NotImplementedError

    def items(self) -> list[tuple]:
        raise NotImplementedError

    def __iter__(self) -> Iterator:
        raise NotImplementedError
