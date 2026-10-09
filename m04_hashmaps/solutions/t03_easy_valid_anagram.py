"""
Task 03 · Easy · Valid Anagram  (SOLUTION)

Count up for s, count down for t; every count must end at zero.
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        remaining = counts.get(ch, 0)
        if remaining == 0:  # t has a char s doesn't (or too many of it)
            return False
        counts[ch] = remaining - 1
    return True
