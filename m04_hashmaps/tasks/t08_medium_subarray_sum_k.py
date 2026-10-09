"""
Task 08 · Medium · Subarray Sum Equals K  (LeetCode #560)

Given a list of integers `nums` (may include negatives and zeros) and an
integer k, return the number of CONTIGUOUS non-empty subarrays whose sum is k.

Checking every subarray is O(n^2) and times out. Combine PREFIX SUMS with a
hash map of "how many times have I seen this prefix sum so far?".

Example 1:
    Input:  nums = [1, 1, 1], k = 2
    Output: 2             ([1,1] at 0..1 and 1..2)

Example 2:
    Input:  nums = [1, 2, 3], k = 3
    Output: 2             ([1,2] and [3])

Constraints:
    - 0 <= len(nums) <= 10^5
    - -1000 <= nums[i] <= 1000
    - -10^7 <= k <= 10^7

Target: O(n) time, O(n) space.
"""


def subarray_sum(nums: list[int], k: int) -> int:
    raise NotImplementedError
