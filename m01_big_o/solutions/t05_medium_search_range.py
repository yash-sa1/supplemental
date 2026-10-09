"""
Task 05 · Medium · Find First and Last Position of Element  (SOLUTION)

Two binary searches. The trick: when arr[mid] == target, don't stop —
record it and keep searching left (for first) or right (for last).
"""
from collections.abc import Sequence


def _find_edge(arr: Sequence[int], target: int, leftmost: bool) -> int:
    lo, hi = 0, len(arr) - 1
    found = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        value = arr[mid]
        if value < target:
            lo = mid + 1
        elif value > target:
            hi = mid - 1
        else:
            found = mid
            if leftmost:
                hi = mid - 1  # maybe an earlier copy exists
            else:
                lo = mid + 1  # maybe a later copy exists
    return found


def search_range(arr: Sequence[int], target: int) -> list[int]:
    first = _find_edge(arr, target, leftmost=True)
    if first == -1:
        return [-1, -1]
    return [first, _find_edge(arr, target, leftmost=False)]
