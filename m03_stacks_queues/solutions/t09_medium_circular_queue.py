"""
Task 09 · Medium · Design Circular Queue  (SOLUTION)

Track `head` (index of the front) and `count`. The back slot is derived:
    back index      = (head + count - 1) % capacity
    next free slot  = (head + count) % capacity
Keeping a count avoids the classic "is head == tail empty or full?" ambiguity.
"""
from typing import Any


class CircularQueue:
    def __init__(self, k: int):
        if k < 1:
            raise ValueError("capacity must be at least 1")
        self._buf: list = [None] * k
        self._cap = k
        self._head = 0
        self._count = 0

    def enqueue(self, val: Any) -> bool:
        if self._count == self._cap:
            return False
        self._buf[(self._head + self._count) % self._cap] = val
        self._count += 1
        return True

    def dequeue(self) -> Any:
        if self._count == 0:
            raise IndexError("dequeue from empty queue")
        val = self._buf[self._head]
        self._buf[self._head] = None  # drop the reference
        self._head = (self._head + 1) % self._cap
        self._count -= 1
        return val

    def front(self) -> Any:
        if self._count == 0:
            raise IndexError("front of empty queue")
        return self._buf[self._head]

    def rear(self) -> Any:
        if self._count == 0:
            raise IndexError("rear of empty queue")
        return self._buf[(self._head + self._count - 1) % self._cap]

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == self._cap

    def __len__(self) -> int:
        return self._count
