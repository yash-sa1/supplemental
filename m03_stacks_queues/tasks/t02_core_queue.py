"""
Task 02 · Core · Build a Queue (linked-list backed)

A queue is FIFO: first in, first out. A Python list is a BAD queue:
list.pop(0) shifts every other element, so it's O(n).

Implement a queue with O(1) enqueue AND dequeue using linked nodes — reuse
ListNode from m02_linked_lists.framework. Keep a pointer to both ends:
enqueue at the tail, dequeue from the head.
Don't use collections.deque (that's the answer you'd use in real code, but
the point here is to build one).

Required behaviour:
    q.enqueue(val)   O(1)  add to the back
    q.dequeue()      O(1)  remove + return the front value; IndexError if empty
    q.peek()         O(1)  front value without removing; IndexError if empty
    q.is_empty()     O(1)
    len(q)           O(1)
    q.to_list()      values front -> back

Example:
    q = LinkedQueue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    q.dequeue()  -> 1
    q.peek()     -> 2
"""

from typing import Any

from m02_linked_lists.framework import ListNode


class LinkedQueue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, val: Any) -> None:
        raise NotImplementedError

    def dequeue(self) -> Any:
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def to_list(self) -> list:
        raise NotImplementedError
