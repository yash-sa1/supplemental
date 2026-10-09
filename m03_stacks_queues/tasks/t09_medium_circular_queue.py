"""
Task 09 · Medium · Design Circular Queue  (LeetCode #622)

A circular queue (ring buffer) is a fixed-capacity FIFO stored in a
fixed-size array. The back "wraps around" to index 0 once it reaches the end,
reusing slots freed by dequeues — no shifting, everything O(1).

    capacity = 4, after enqueue 1,2,3,4 then dequeue twice then enqueue 5:
        slots: [5, _, 3, 4]      front -> index 2, back -> index 0

Implement CircularQueue(k) using a list of length k allocated ONCE in
__init__ (plus index/count bookkeeping). Don't grow it and don't use deque.

    q.enqueue(val) -> bool   add to back; False (and no change) if full
    q.dequeue()    -> value  remove + return the front; IndexError if empty
    q.front()      -> value  front without removing;    IndexError if empty
    q.rear()       -> value  back without removing;     IndexError if empty
    q.is_empty()   -> bool
    q.is_full()    -> bool
    len(q)         -> int

If k < 1 raise ValueError.

Example:
    q = CircularQueue(3)
    q.enqueue(1), q.enqueue(2), q.enqueue(3)  -> True, True, True
    q.enqueue(4)  -> False     (full)
    q.rear()      -> 3
    q.dequeue()   -> 1
    q.enqueue(4)  -> True      (wrapped into the freed slot)
    q.rear()      -> 4

Target: every operation O(1).
"""
from typing import Any


class CircularQueue:
    def __init__(self, k: int):
        raise NotImplementedError

    def enqueue(self, val: Any) -> bool:
        raise NotImplementedError

    def dequeue(self) -> Any:
        raise NotImplementedError

    def front(self) -> Any:
        raise NotImplementedError

    def rear(self) -> Any:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
