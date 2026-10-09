"""
Task 04 · Easy · Integer Square Root  (SOLUTION)

"Binary search on the answer": the predicate mid*mid <= x is True for a
prefix of candidates and False after. Find the LAST candidate where it's True.
"""


def sqrt_floor(x: int) -> int:
    if x < 0:
        raise ValueError("x must be non-negative")
    lo, hi = 0, x
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            answer = mid  # mid works; try for something bigger
            lo = mid + 1
        else:
            hi = mid - 1
    return answer
