"""
Task 07 · Medium · Find Peak Element  (SOLUTION)

If arr[mid] < arr[mid + 1] we're on an uphill slope, so a peak must exist to
the right (the climb has to stop somewhere, worst case at the -inf edge).
Otherwise a peak exists at mid or to its left. Shrink until lo == hi.
"""
from collections.abc import Sequence


def find_peak(arr: Sequence[int]) -> int:
    lo, hi = 0, len(arr) - 1  # invariant: a peak exists in [lo, hi]
    while lo < hi:
        mid = (lo + hi) // 2  # mid < hi, so mid + 1 is always in range
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
