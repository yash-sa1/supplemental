"""
Task 05 · Easy · Backspace String Compare  (SOLUTION)

Simulate the editor with a stack: letters push, '#' pops (if anything's there).
"""


def _typed(text: str) -> list[str]:
    stack = []
    for ch in text:
        if ch == "#":
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return stack


def backspace_compare(s: str, t: str) -> bool:
    return _typed(s) == _typed(t)
