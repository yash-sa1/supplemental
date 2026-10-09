"""
Task 01 · Core · Build a Singly Linked List  (SOLUTION)
"""
from collections.abc import Iterator
from typing import Any, Optional

from m02_linked_lists.framework import ListNode


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def prepend(self, val: Any) -> None:
        self.head = ListNode(val, self.head)
        if self.tail is None:  # list was empty: new node is also the tail
            self.tail = self.head
        self._size += 1

    def append(self, val: Any) -> None:
        node = ListNode(val)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def _node_before(self, index: int) -> ListNode:
        """Node at position index - 1 (caller guarantees 1 <= index <= size)."""
        node = self.head
        for _ in range(index - 1):
            node = node.next
        return node

    def insert(self, index: int, val: Any) -> None:
        if not 0 <= index <= self._size:
            raise IndexError(f"insert index {index} out of range for size {self._size}")
        if index == 0:
            self.prepend(val)
        elif index == self._size:
            self.append(val)
        else:
            prev = self._node_before(index)
            prev.next = ListNode(val, prev.next)
            self._size += 1

    def get(self, index: int) -> Any:
        if not 0 <= index < self._size:
            raise IndexError(f"index {index} out of range for size {self._size}")
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def pop_front(self) -> Any:
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head is None:  # removed the only node
            self.tail = None
        self._size -= 1
        return node.val

    def remove_at(self, index: int) -> Any:
        if not 0 <= index < self._size:
            raise IndexError(f"index {index} out of range for size {self._size}")
        if index == 0:
            return self.pop_front()
        prev = self._node_before(index)
        target = prev.next
        prev.next = target.next
        if target is self.tail:  # removed the last node: tail moves back
            self.tail = prev
        self._size -= 1
        return target.val

    def remove(self, val: Any) -> bool:
        prev, node = None, self.head
        while node is not None:
            if node.val == val:
                if prev is None:
                    self.pop_front()
                else:
                    prev.next = node.next
                    if node is self.tail:
                        self.tail = prev
                    self._size -= 1
                return True
            prev, node = node, node.next
        return False

    def find(self, val: Any) -> int:
        for i, v in enumerate(self):
            if v == val:
                return i
        return -1

    def __contains__(self, val: Any) -> bool:
        return self.find(val) != -1

    def __iter__(self) -> Iterator[Any]:
        node = self.head
        while node is not None:
            yield node.val
            node = node.next

    def to_list(self) -> list:
        return list(self)
