"""
Task 02 · Easy · Two Sum  (LeetCode #1)

Given a list of integers `nums` and an integer `target`, return the indices
[i, j] (with i < j) of the two numbers that add up to target.
You may not use the same element twice. If there's no such pair, return [].

If several pairs work, return the one whose SECOND index j is smallest
(i.e. the first pair you can complete scanning left to right); if that j
pairs with several earlier i, use the earliest i.

Example 1:
    Input:  nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Example 2:
    Input:  nums = [3, 2, 4], target = 6
    Output: [1, 2]

Example 3:
    Input:  nums = [3, 3], target = 6
    Output: [0, 1]

Constraints:
    - 0 <= len(nums) <= 10^5
    - -10^9 <= nums[i], target <= 10^9

Target: O(n) time with a hash map (checking every pair is O(n^2) and times out).
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError
