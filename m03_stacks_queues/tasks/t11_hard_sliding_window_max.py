"""
Task 11 · Hard · Sliding Window Maximum  (LeetCode #239)

Given a list `nums` and a window size k, a window slides from the far left to
the far right one position at a time. Return a list of the maximum value in
each window position.

Recomputing max() for every window is O(n*k) and times out. Use a MONOTONIC
DEQUE of indices (collections.deque is allowed here).

Example 1:
    Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [3, 3, 5, 5, 6, 7]

        Window                    Max
        [1  3  -1] -3  5  3  6  7   3
         1 [3  -1  -3] 5  3  6  7   3
         1  3 [-1  -3  5] 3  6  7   5
         1  3  -1 [-3  5  3] 6  7   5
         1  3  -1  -3 [5  3  6] 7   6
         1  3  -1  -3  5 [3  6  7]  7

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= k <= len(nums) <= 10^5  (raise ValueError if k is outside 1..len(nums))

Target: O(n) time, O(k) extra space.
"""


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError
