"""
Task 06 · Medium · Min Stack  (SOLUTION)

Store (value, min_so_far) pairs. Each entry remembers the minimum of itself
and everything below it, so popping automatically "restores" the old minimum.
"""


class MinStack:
    def __init__(self):
        self._items: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        current_min = min(val, self._items[-1][1]) if self._items else val
        self._items.append((val, current_min))

    def pop(self) -> int:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()[0]

    def top(self) -> int:
        if not self._items:
            raise IndexError("top of empty stack")
        return self._items[-1][0]

    def get_min(self) -> int:
        if not self._items:
            raise IndexError("min of empty stack")
        return self._items[-1][1]

    def __len__(self) -> int:
        return len(self._items)
