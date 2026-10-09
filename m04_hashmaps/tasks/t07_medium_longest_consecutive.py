"""
Task 07 · Medium · Longest Consecutive Sequence  (LeetCode #128)

Given an UNSORTED list of integers, return the length of the longest run of
consecutive integers (x, x+1, x+2, ...) that appear in it, in any order.

Must be O(n): no sorting.

Example 1:
    Input:  [100, 4, 200, 1, 3, 2]
    Output: 4            (1, 2, 3, 4)

Example 2:
    Input:  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9            (0 .. 8)

Constraints:
    - 0 <= len(nums) <= 10^5
    - -10^9 <= nums[i] <= 10^9

Target: O(n) time using a set. Hint: only start counting from numbers that
are the START of a run.
"""


def longest_consecutive(nums: list[int]) -> int:
    raise NotImplementedError
