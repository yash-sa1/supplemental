"""
Task 08 · Hard · Median of Two Sorted Arrays  (LeetCode #4)

Given two sorted (ascending) sequences `a` and `b`, return the median of all
their elements combined, as a float.

    - odd total length  -> the middle element
    - even total length -> the average of the two middle elements

Merging the arrays is O(m + n); the tests require O(log(min(m, n))).
If both arrays are empty, raise ValueError.

Example 1:
    Input:  a = [1, 3], b = [2]
    Output: 2.0

Example 2:
    Input:  a = [1, 2], b = [3, 4]
    Output: 2.5

Constraints:
    - 0 <= len(a), len(b) <= 10^6
    - Values are integers; duplicates allowed.

Target: O(log(min(m, n))) time, O(1) space.
"""
from collections.abc import Sequence


def find_median_sorted_arrays(a: Sequence[int], b: Sequence[int]) -> float:
    raise NotImplementedError
