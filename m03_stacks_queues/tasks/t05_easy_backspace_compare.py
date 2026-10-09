"""
Task 05 · Easy · Backspace String Compare  (LeetCode #844)

Given two strings s and t, return True if they're equal when both are typed
into empty text editors. '#' means a backspace character.
Backspacing an empty editor leaves it empty.

Example 1:
    Input:  s = "ab#c", t = "ad#c"
    Output: True        (both become "ac")

Example 2:
    Input:  s = "ab##", t = "c#d#"
    Output: True        (both become "")

Example 3:
    Input:  s = "a#c", t = "b"
    Output: False       ("c" vs "b")

Constraints:
    - 0 <= len(s), len(t) <= 10^5
    - Strings contain lowercase letters and '#'.

Target: O(n + m) time. (Follow-up: O(1) space by walking backwards.)
"""


def backspace_compare(s: str, t: str) -> bool:
    raise NotImplementedError
