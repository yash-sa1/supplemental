"""
Task 09 · Hard · LRU Cache  (SOLUTION)

    dict:   key -> node              (O(1) lookup)
    list:   HEAD <-> least ... most recent <-> TAIL   (O(1) reorder/evict)

Each node stores its key too, so when we evict the LRU node we know which
dict entry to delete.
"""
from typing import Any, Hashable

from m02_linked_lists.framework import DListNode


class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._capacity = capacity
        self._nodes: dict[Hashable, DListNode] = {}
        self._head = DListNode()  # sentinel before the least recent
        self._tail = DListNode()  # sentinel after the most recent
        self._head.next = self._tail
        self._tail.prev = self._head

    def _unlink(self, node: DListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append_most_recent(self, node: DListNode) -> None:
        last = self._tail.prev
        last.next = node
        node.prev = last
        node.next = self._tail
        self._tail.prev = node

    def get(self, key: Hashable) -> Any:
        node = self._nodes.get(key)
        if node is None:
            return -1
        self._unlink(node)
        self._append_most_recent(node)
        return node.val[1]

    def put(self, key: Hashable, value: Any) -> None:
        node = self._nodes.get(key)
        if node is not None:
            node.val = (key, value)
            self._unlink(node)
            self._append_most_recent(node)
            return
        if len(self._nodes) == self._capacity:
            lru = self._head.next
            self._unlink(lru)
            del self._nodes[lru.val[0]]
        node = DListNode((key, value))
        self._nodes[key] = node
        self._append_most_recent(node)

    def __len__(self) -> int:
        return len(self._nodes)
