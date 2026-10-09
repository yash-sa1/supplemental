"""
Task 09 · Hard · LRU Cache  (LeetCode #146)

Design a Least Recently Used cache with a fixed capacity.

    cache = LRUCache(capacity)
    cache.get(key)        -> value, or -1 if the key isn't present.
                             Counts as a USE (key becomes most recently used).
    cache.put(key, value) -> insert or update. Counts as a use.
                             If inserting a NEW key makes the size exceed
                             capacity, evict the LEAST recently used key first.
    len(cache)            -> number of keys stored

Both get and put must be O(1). The classic design is a dict (key -> node)
plus a doubly linked list ordered by recency — use DListNode from
m02_linked_lists.framework. A dict is allowed here; OrderedDict is not
(that would do the whole task for you).

Raise ValueError if capacity < 1.

Example:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)      -> 1     (order now: 2 is least recent, 1 most recent)
    cache.put(3, 3)   # evicts key 2
    cache.get(2)      -> -1
    cache.put(4, 4)   # evicts key 1
    cache.get(1)      -> -1
    cache.get(3)      -> 3
    cache.get(4)      -> 4

Constraints:
    - 1 <= capacity <= 10^5, up to 2 * 10^5 calls.
"""
from typing import Any, Hashable

from m02_linked_lists.framework import DListNode


class LRUCache:
    def __init__(self, capacity: int):
        raise NotImplementedError

    def get(self, key: Hashable) -> Any:
        raise NotImplementedError

    def put(self, key: Hashable, value: Any) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
