"""
Task 06 · Medium · Search in Rotated Sorted Array  (SOLUTION)

Key insight: cut a rotated array at any mid and at least one half is
properly sorted. Check whether target lies inside the sorted half's range;
if so search there, otherwise search the other half.
"""
from collections.abc import Sequence


def search_rotated(arr: Sequence[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        lo_val = arr[lo]
        if lo_val <= mid_val:  # left half [lo..mid] is sorted
            if lo_val <= target < mid_val:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half [mid..hi] is sorted
            hi_val = arr[hi]
            if mid_val < target <= hi_val:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
