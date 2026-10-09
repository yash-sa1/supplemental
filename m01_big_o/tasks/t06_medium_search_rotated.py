"""
Task 06 · Medium · Search in Rotated Sorted Array  (LeetCode #33)

An ascending array of DISTINCT integers was possibly rotated at an unknown
pivot, e.g. [0, 1, 2, 4, 5, 6, 7] -> [4, 5, 6, 7, 0, 1, 2].

Given the rotated array `arr` and a `target`, return the index of target,
or -1 if it's not present.

Example 1:
    Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Example 2:
    Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1

Example 3:
    Input:  arr = [1], target = 0
    Output: -1

Constraints:
    - 0 <= len(arr) <= 10^6
    - All values are distinct.
    - arr is an ascending array rotated by some k (0 <= k < len(arr)).

Target: O(log n) time, O(1) space.
"""
from collections.abc import Sequence


def search_rotated(arr: Sequence[int], target: int) -> int:
    raise NotImplementedError
