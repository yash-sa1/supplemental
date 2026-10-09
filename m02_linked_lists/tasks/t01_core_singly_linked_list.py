"""
Task 01 · Core · Build a Singly Linked List

Implement a SinglyLinkedList class on top of the given ListNode
(from m02_linked_lists.framework). Don't use a Python list internally —
the nodes ARE the storage.

Required attributes:
    self.head   first ListNode, or None when empty. The tests walk this chain
                directly, so it must always be correct.

Required behaviour (n = number of elements):
    len(sll)             O(1)  (keep a counter, don't walk the list)
    sll.is_empty()       O(1)
    sll.prepend(val)     O(1)  add at the front
    sll.append(val)      O(1)  add at the back  -> you'll need a tail pointer
    sll.insert(i, val)   O(i)  insert so the new value ends up at index i;
                               valid i is 0..len inclusive, else IndexError
    sll.get(i)           O(i)  value at index i; IndexError if i < 0 or i >= len
    sll.pop_front()      O(1)  remove and return first value; IndexError if empty
    sll.remove_at(i)     O(i)  remove and return value at index i; IndexError if invalid
    sll.remove(val)      O(n)  remove FIRST node with this value; return True if
                               something was removed, else False
    sll.find(val)        O(n)  index of first occurrence, or -1
    val in sll           O(n)  (__contains__)
    for v in sll         O(n)  (__iter__ yields values front to back)
    sll.to_list()        O(n)  plain Python list of the values

Example:
    sll = SinglyLinkedList()
    sll.append(2); sll.append(3); sll.prepend(1)   # 1 -> 2 -> 3
    sll.insert(1, 9)                               # 1 -> 9 -> 2 -> 3
    sll.remove_at(3)  -> 3                         # 1 -> 9 -> 2
    len(sll)          -> 3

Watch out: whenever you remove the LAST node, the tail pointer must move too.
"""
from collections.abc import Iterator
from typing import Any, Optional

from m02_linked_lists.framework import ListNode


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        # add any other attributes you need (tail, size, ...)

    def __len__(self) -> int:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def prepend(self, val: Any) -> None:
        raise NotImplementedError

    def append(self, val: Any) -> None:
        raise NotImplementedError

    def insert(self, index: int, val: Any) -> None:
        raise NotImplementedError

    def get(self, index: int) -> Any:
        raise NotImplementedError

    def pop_front(self) -> Any:
        raise NotImplementedError

    def remove_at(self, index: int) -> Any:
        raise NotImplementedError

    def remove(self, val: Any) -> bool:
        raise NotImplementedError

    def find(self, val: Any) -> int:
        raise NotImplementedError

    def __contains__(self, val: Any) -> bool:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        raise NotImplementedError

    def to_list(self) -> list:
        raise NotImplementedError
