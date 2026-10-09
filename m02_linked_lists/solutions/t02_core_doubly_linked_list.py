"""
Task 02 · Core · Build a Doubly Linked List  (SOLUTION)

Uses two sentinel nodes so real nodes always have real neighbours:
    HEAD <-> a <-> b <-> c <-> TAIL
"""
from collections.abc import Iterator
from typing import Any

from m02_linked_lists.framework import DListNode


class DoublyLinkedList:
    def __init__(self):
        self._head = DListNode("HEAD")
        self._tail = DListNode("TAIL")
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    # --- two primitives everything else is built on --------------------------

    def _link_after(self, node: DListNode, val: Any) -> None:
        new = DListNode(val, prev=node, next=node.next)
        node.next.prev = new
        node.next = new
        self._size += 1

    def _unlink(self, node: DListNode) -> Any:
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node.val

    def _node_at(self, index: int) -> DListNode:
        """Walk from whichever end is closer. index may equal size (returns TAIL)."""
        if index <= self._size // 2:
            node = self._head.next
            for _ in range(index):
                node = node.next
        else:
            node = self._tail
            for _ in range(self._size - index):
                node = node.prev
        return node

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError(f"index {index} out of range for size {self._size}")

    # --- public API ----------------------------------------------------------

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def push_front(self, val: Any) -> None:
        self._link_after(self._head, val)

    def push_back(self, val: Any) -> None:
        self._link_after(self._tail.prev, val)

    def pop_front(self) -> Any:
        if self._size == 0:
            raise IndexError("pop from empty list")
        return self._unlink(self._head.next)

    def pop_back(self) -> Any:
        if self._size == 0:
            raise IndexError("pop from empty list")
        return self._unlink(self._tail.prev)

    def peek_front(self) -> Any:
        if self._size == 0:
            raise IndexError("peek at empty list")
        return self._head.next.val

    def peek_back(self) -> Any:
        if self._size == 0:
            raise IndexError("peek at empty list")
        return self._tail.prev.val

    def insert(self, index: int, val: Any) -> None:
        if not 0 <= index <= self._size:
            raise IndexError(f"insert index {index} out of range for size {self._size}")
        self._link_after(self._node_at(index).prev, val)

    def remove_at(self, index: int) -> Any:
        self._check_index(index)
        return self._unlink(self._node_at(index))

    def get(self, index: int) -> Any:
        self._check_index(index)
        return self._node_at(index).val

    def __iter__(self) -> Iterator[Any]:
        node = self._head.next
        while node is not self._tail:
            yield node.val
            node = node.next

    def __reversed__(self) -> Iterator[Any]:
        node = self._tail.prev
        while node is not self._head:
            yield node.val
            node = node.prev

    def to_list(self) -> list:
        return list(self)
