"""
Task 05 · Medium · Find First and Last Position of Element  (LeetCode #34)

Given a sequence `arr` sorted in ascending order (duplicates allowed), return
[first_index, last_index] of `target`. If target is not present, return [-1, -1].

You must do this in O(log n) — even when the whole array is the target value.
Finding one match and then walking left/right is O(n) in that case and the
tests will catch it.

Example 1:
    Input:  arr = [5, 7, 7, 8, 8, 10], target = 8
    Output: [3, 4]

Example 2:
    Input:  arr = [5, 7, 7, 8, 8, 10], target = 6
    Output: [-1, -1]

Example 3:
    Input:  arr = [], target = 0
    Output: [-1, -1]

Constraints:
    - 0 <= len(arr) <= 10^6
    - arr is sorted ascending.

Target: O(log n) time, O(1) space.
"""
from collections.abc import Sequence


def search_range(arr: Sequence[int], target: int) -> list[int]:
    raise NotImplementedError
