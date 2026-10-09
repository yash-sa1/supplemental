"""
Task 05 · Medium · Group Anagrams  (LeetCode #49)

Given a list of strings, group the anagrams together. Return a list of
groups (each group a list of strings). Groups can be in any order, and
strings within a group can be in any order.

Duplicates stay: ["a", "a"] -> [["a", "a"]].

Example 1:
    Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]   (any order)

Example 2:
    Input:  [""]
    Output: [[""]]

Example 3:
    Input:  []
    Output: []

Constraints:
    - 0 <= len(strs) <= 10^4
    - 0 <= len(strs[i]) <= 100

Target: O(n * k log k) with sorted-string keys, or O(n * k) with count keys
(n = number of strings, k = max length). Hint: what makes a good dict KEY?
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    raise NotImplementedError
