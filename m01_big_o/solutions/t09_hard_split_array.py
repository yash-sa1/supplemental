"""
Task 09 · Hard · Split Array Largest Sum  (SOLUTION)

Binary search on the ANSWER. For a candidate cap C, greedily pack elements
into pieces without exceeding C and count the pieces needed. If that count
<= k, C is feasible (and so is anything bigger) — a monotonic predicate.
The answer lies in [max(nums), sum(nums)]; find the smallest feasible C.
"""


def _pieces_needed(nums: list[int], cap: int) -> int:
    pieces, current = 1, 0
    for x in nums:
        if current + x > cap:
            pieces += 1
            current = x
        else:
            current += x
    return pieces


def split_array(nums: list[int], k: int) -> int:
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if _pieces_needed(nums, mid) <= k:
            hi = mid  # feasible: try a smaller cap
        else:
            lo = mid + 1  # too small a cap
    return lo
