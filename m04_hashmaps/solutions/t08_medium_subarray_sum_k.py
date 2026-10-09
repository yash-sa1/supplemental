"""
Task 08 · Medium · Subarray Sum Equals K  (SOLUTION)

sum(nums[i+1 .. j]) == prefix[j] - prefix[i]. So a subarray ending at j sums
to k exactly when some earlier prefix equals prefix[j] - k. Count how many
earlier prefixes have that value with a dict. Seed {0: 1} for the empty prefix
(subarrays that start at index 0).
"""


def subarray_sum(nums: list[int], k: int) -> int:
    seen: dict[int, int] = {0: 1}
    prefix = 0
    count = 0
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count
