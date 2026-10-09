"""
Task 08 · Hard · Median of Two Sorted Arrays  (SOLUTION)

Binary search for a PARTITION instead of a value. Cut `a` after i elements and
`b` after j elements so that the left side holds half the total:
    i + j == (m + n + 1) // 2
The partition is correct when everything on the left <= everything on the right:
    a[i-1] <= b[j]  and  b[j-1] <= a[i]
Then the median comes from the max of the left side / min of the right side.
Searching over the shorter array keeps it O(log(min(m, n))).
"""
import math
from collections.abc import Sequence


def find_median_sorted_arrays(a: Sequence[int], b: Sequence[int]) -> float:
    if len(a) > len(b):
        a, b = b, a  # binary search over the shorter one
    m, n = len(a), len(b)
    if m + n == 0:
        raise ValueError("both arrays are empty")

    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2  # elements taken from a
        j = half - i        # elements taken from b
        a_left = a[i - 1] if i > 0 else -math.inf
        a_right = a[i] if i < m else math.inf
        b_left = b[j - 1] if j > 0 else -math.inf
        b_right = b[j] if j < n else math.inf

        if a_left <= b_right and b_left <= a_right:
            left_max = max(a_left, b_left)
            if (m + n) % 2 == 1:
                return float(left_max)
            return (left_max + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1  # took too many from a
        else:
            lo = i + 1  # took too few from a

    raise AssertionError("unreachable for sorted input")
