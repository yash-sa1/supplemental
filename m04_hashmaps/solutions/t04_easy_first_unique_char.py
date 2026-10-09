"""
Task 04 · Easy · First Unique Character in a String  (SOLUTION)

Pass 1: count every character. Pass 2: first index whose count is 1.
"""


def first_uniq_char(s: str) -> int:
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
