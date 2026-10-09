"""
Task 01 · Core · Build a Stack  (SOLUTION)
"""
from typing import Any


class Stack:
    def __init__(self):
        self._items: list = []  # index -1 is the top

    def push(self, val: Any) -> None:
        self._items.append(val)

    def pop(self) -> Any:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)

    def to_list(self) -> list:
        return list(self._items)  # a copy, so callers can't corrupt the stack
