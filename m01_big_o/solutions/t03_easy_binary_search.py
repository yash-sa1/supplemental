"""
Task 03 · Easy · Binary Search  (SOLUTION)
"""
from collections.abc import Sequence


def binary_search(arr: Sequence[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1  # search space is the CLOSED interval [lo, hi]
    while lo <= hi:  # <= because a 1-element interval still needs checking
        mid = (lo + hi) // 2
        value = arr[mid]
        if value == target:
            return mid
        if value < target:
            lo = mid + 1  # target is strictly right of mid
        else:
            hi = mid - 1  # target is strictly left of mid
    return -1


def binary_search_recursive(arr: Sequence[int], target: int) -> int:
    def helper(lo: int, hi: int) -> int:
        if lo > hi:  # empty interval
            return -1
        mid = (lo + hi) // 2
        value = arr[mid]
        if value == target:
            return mid
        if value < target:
            return helper(mid + 1, hi)
        return helper(lo, mid - 1)

    return helper(0, len(arr) - 1)
