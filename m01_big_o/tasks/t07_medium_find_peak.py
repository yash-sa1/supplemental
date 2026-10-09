"""
Task 07 · Medium · Find Peak Element  (LeetCode #162)

A peak element is strictly greater than its neighbours. Given `arr` where
no two ADJACENT elements are equal, return the index of ANY peak.

Imagine arr[-1] = arr[n] = -infinity, so the first/last element can be a
peak if it beats its one real neighbour.

Example 1:
    Input:  arr = [1, 2, 3, 1]
    Output: 2

Example 2:
    Input:  arr = [1, 2, 1, 3, 5, 6, 4]
    Output: 1 or 5     (either peak is accepted)

Constraints:
    - 1 <= len(arr) <= 10^6
    - arr[i] != arr[i + 1] for all valid i

Target: O(log n) time, O(1) space. (The array is NOT sorted — think about
what comparing arr[mid] with arr[mid + 1] tells you.)
"""
from collections.abc import Sequence


def find_peak(arr: Sequence[int]) -> int:
    raise NotImplementedError
