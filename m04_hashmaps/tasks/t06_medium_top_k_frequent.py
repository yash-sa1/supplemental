"""
Task 06 · Medium · Top K Frequent Elements  (LeetCode #347)

Given a list of integers `nums` and an integer k, return the k most frequent
elements, in any order.

If there's a tie at the cut-off (e.g. two values share the k-th highest
frequency), prefer the SMALLER value so the answer is unique.

Example 1:
    Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]

Example 2:
    Input:  nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= len(nums) <= 10^5
    - 1 <= k <= number of distinct values

Target: better than O(n log n). Count with a hash map, then use "bucket sort"
by frequency (a list where index = frequency) for O(n), or a heap for O(n log k).
Don't use collections.Counter.most_common.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError
