"""
Task 03 · Easy · Valid Anagram  (LeetCode #242)

Given two strings s and t, return True if t is an anagram of s (uses exactly
the same characters the same number of times), else False.

Count characters with a hash map instead of sorting. Don't use
collections.Counter — build the counts yourself.

Example 1:
    Input:  s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input:  s = "rat", t = "car"
    Output: False

Constraints:
    - 0 <= len(s), len(t) <= 10^5
    - Any unicode characters; comparison is case-sensitive.

Target: O(n) time, O(k) space where k = number of distinct characters.
"""


def is_anagram(s: str, t: str) -> bool:
    raise NotImplementedError
