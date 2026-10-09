"""
Task 02 · Core · Build a Queue (linked-list backed)  (SOLUTION)

    head (front, dequeue here) -> ... -> tail (back, enqueue here)
"""
from typing import Any

from m02_linked_lists.framework import ListNode


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, val: Any) -> None:
        node = ListNode(val)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self) -> Any:
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        node = self._head
        self._head = node.next
        if self._head is None:  # queue is now empty: tail must not dangle
            self._tail = None
        self._size -= 1
        return node.val

    def peek(self) -> Any:
        if self._head is None:
            raise IndexError("peek at empty queue")
        return self._head.val

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def to_list(self) -> list:
        out, node = [], self._head
        while node is not None:
            out.append(node.val)
            node = node.next
        return out
