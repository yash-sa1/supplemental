"""
Task 04 · Easy · Implement Queue using Stacks  (LeetCode #232)

Implement a FIFO queue using ONLY two stacks (Python lists where you only
use append(), pop() with no argument, [-1] to peek, and len()).

    q.push(x)    add x to the back
    q.pop()      remove + return the front element; IndexError if empty
    q.peek()     return the front element;              IndexError if empty
    q.empty()    True if the queue is empty

Every operation must be AMORTISED O(1): over any sequence of n operations the
total work is O(n). (Moving everything between stacks on every call is O(n)
per operation and will time out.)

Example:
    q = MyQueue()
    q.push(1); q.push(2)
    q.peek()  -> 1
    q.pop()   -> 1
    q.empty() -> False
"""
from typing import Any


class MyQueue:
    def __init__(self):
        raise NotImplementedError

    def push(self, x: Any) -> None:
        raise NotImplementedError

    def pop(self) -> Any:
        raise NotImplementedError

    def peek(self) -> Any:
        raise NotImplementedError

    def empty(self) -> bool:
        raise NotImplementedError
