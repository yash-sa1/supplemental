"""
Task 06 · Medium · Min Stack  (LeetCode #155)

Design a stack that also returns its minimum element in constant time.

    s.push(val)    push val
    s.pop()        remove + return the top; IndexError if empty
    s.top()        return the top;          IndexError if empty
    s.get_min()    return the smallest value currently in the stack; IndexError if empty
    len(s)

ALL operations must be O(1). Scanning for the minimum is O(n) and will time out.

Example:
    s = MinStack()
    s.push(-2); s.push(0); s.push(-3)
    s.get_min() -> -3
    s.pop()     -> -3
    s.top()     -> 0
    s.get_min() -> -2

Constraints:
    - Up to 3 * 10^5 operations; values are ints.
"""


class MinStack:
    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def get_min(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
