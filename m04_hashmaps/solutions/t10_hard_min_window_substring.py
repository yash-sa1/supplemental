"""
Task 10 · Hard · Minimum Window Substring  (SOLUTION)

`need[c]` = how many more c's the window needs (can go negative = surplus).
`missing` = total characters of t still not covered. The window is valid
exactly when missing == 0. Every index enters and leaves the window once.
"""


def min_window(s: str, t: str) -> str:
    if not t or len(t) > len(s):
        return ""
    need: dict[str, int] = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)

    best_start, best_len = 0, len(s) + 1
    left = 0
    for right, ch in enumerate(s):
        if need.get(ch, 0) > 0:
            missing -= 1
        need[ch] = need.get(ch, 0) - 1

        while missing == 0:  # valid: record, then try to shrink from the left
            if right - left + 1 < best_len:  # strict < keeps the leftmost on ties
                best_start, best_len = left, right - left + 1
            out = s[left]
            need[out] += 1
            if need[out] > 0:  # we just dropped a character we needed
                missing += 1
            left += 1

    return s[best_start : best_start + best_len] if best_len <= len(s) else ""
