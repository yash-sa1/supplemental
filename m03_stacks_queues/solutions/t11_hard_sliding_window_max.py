"""
Task 11 · Hard · Sliding Window Maximum  (SOLUTION)

The deque holds indices whose values are DECREASING front to back.
    - New value arrives: pop smaller values off the back (they can never be
      a maximum again while the new, larger value is in the window).
    - Front index slid out of the window: pop it off the front.
    - The front is always the current window's max.
Each index enters and leaves once -> O(n).
"""
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    window: deque[int] = deque()
    result = []
    for i, x in enumerate(nums):
        while window and nums[window[-1]] <= x:
            window.pop()
        window.append(i)
        if window[0] <= i - k:  # front has slid out
            window.popleft()
        if i >= k - 1:
            result.append(nums[window[0]])
    return result
