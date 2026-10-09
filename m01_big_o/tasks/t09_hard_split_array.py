"""
Task 09 · Hard · Split Array Largest Sum  (LeetCode #410)

Given a list of non-negative integers `nums` and an integer `k`, split nums
into exactly k non-empty CONTIGUOUS subarrays so that the largest subarray
sum is as small as possible. Return that minimised largest sum.

Example 1:
    Input:  nums = [7, 2, 5, 10, 8], k = 2
    Output: 18         ([7, 2, 5] and [10, 8])

Example 2:
    Input:  nums = [1, 2, 3, 4, 5], k = 2
    Output: 9          ([1, 2, 3] and [4, 5])

Constraints:
    - 1 <= len(nums) <= 10^4
    - 0 <= nums[i] <= 10^6
    - 1 <= k <= min(50, len(nums))

Target: O(n log(sum(nums))) time. A DP over all split points is O(k * n^2)
and will time out on the big test.
"""


def split_array(nums: list[int], k: int) -> int:
    raise NotImplementedError
