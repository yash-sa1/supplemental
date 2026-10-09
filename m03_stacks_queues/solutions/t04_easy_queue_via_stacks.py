"""
Task 04 · Easy · Implement Queue using Stacks  (SOLUTION)

`inbox` receives pushes. `outbox` holds elements in reversed (= queue) order.
Only when outbox is empty do we pour inbox into it. Each element is moved at
most once, so the cost is amortised O(1).
"""
from typing import Any


class MyQueue:
    def __init__(self):
        self._inbox: list = []
        self._outbox: list = []

    def push(self, x: Any) -> None:
        self._inbox.append(x)

    def _shift(self) -> None:
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())
        if not self._outbox:
            raise IndexError("queue is empty")

    def pop(self) -> Any:
        self._shift()
        return self._outbox.pop()

    def peek(self) -> Any:
        self._shift()
        return self._outbox[-1]

    def empty(self) -> bool:
        return not self._inbox and not self._outbox
