"""
Task 10 · Hard · Minimum Window Substring  (LeetCode #76)

Given strings s and t, return the SHORTEST substring of s that contains every
character of t (including duplicates: t = "aa" needs two a's). If there's no
such window, return "". If several shortest windows exist, return the
LEFTMOST one. If t is empty, return "".

Example 1:
    Input:  s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Example 2:
    Input:  s = "a", t = "a"
    Output: "a"

Example 3:
    Input:  s = "a", t = "aa"
    Output: ""

Constraints:
    - 0 <= len(s), len(t) <= 10^5
    - Case-sensitive.

Target: O(len(s) + len(t)) with a sliding window: grow the right edge until
the window is valid, then shrink the left edge while it stays valid. Track
"how many characters of t are still missing" with a hash map of counts.
"""


def min_window(s: str, t: str) -> str:
    raise NotImplementedError
