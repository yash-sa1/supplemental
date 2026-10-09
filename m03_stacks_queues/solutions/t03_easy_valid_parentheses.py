"""
Task 03 · Easy · Valid Parentheses  (SOLUTION)

Push openers; on a closer, the top of the stack must be its partner.
At the end the stack must be empty (no unclosed openers).
"""

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack = []
    for ch in s:
        if ch in PAIRS:
            if not stack or stack.pop() != PAIRS[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
