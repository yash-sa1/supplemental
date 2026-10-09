"""
Task 02 · Core · Build a Doubly Linked List

Implement a DoublyLinkedList using the given DListNode (val, prev, next).
Every node links both ways, which makes removing from EITHER end O(1).

Tip: many people use two sentinel ("dummy") nodes, head and tail, that never
hold data. Then every real node always has a real prev and next, and you never
need `if node is None` special cases. Up to you — the tests only use the
public methods below.

Required behaviour:
    len(dll)              O(1)
    dll.is_empty()        O(1)
    dll.push_front(val)   O(1)
    dll.push_back(val)    O(1)
    dll.pop_front()       O(1)  remove + return first value; IndexError if empty
    dll.pop_back()        O(1)  remove + return last value;  IndexError if empty
    dll.peek_front()      O(1)  first value without removing; IndexError if empty
    dll.peek_back()       O(1)  last value without removing;  IndexError if empty
    dll.insert(i, val)    O(n)  new value ends up at index i; 0 <= i <= len, else IndexError
    dll.remove_at(i)      O(n)  remove + return value at i; IndexError if invalid
    dll.get(i)            O(n)  value at i; IndexError if invalid (no negative indices)
    for v in dll          front -> back   (__iter__)
    reversed(dll)         back -> front   (__reversed__, must follow the .prev pointers)
    dll.to_list()         values front -> back

Bonus: get/insert/remove_at can walk from whichever end is closer.
"""
from collections.abc import Iterator
from typing import Any

from m02_linked_lists.framework import DListNode


class DoublyLinkedList:
    def __init__(self):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def push_front(self, val: Any) -> None:
        raise NotImplementedError

    def push_back(self, val: Any) -> None:
        raise NotImplementedError

    def pop_front(self) -> Any:
        raise NotImplementedError

    def pop_back(self) -> Any:
        raise NotImplementedError

    def peek_front(self) -> Any:
        raise NotImplementedError

    def peek_back(self) -> Any:
        raise NotImplementedError

    def insert(self, index: int, val: Any) -> None:
        raise NotImplementedError

    def remove_at(self, index: int) -> Any:
        raise NotImplementedError

    def get(self, index: int) -> Any:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        raise NotImplementedError

    def __reversed__(self) -> Iterator[Any]:
        raise NotImplementedError

    def to_list(self) -> list:
        raise NotImplementedError
