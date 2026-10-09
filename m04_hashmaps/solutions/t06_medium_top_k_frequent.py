"""
Task 06 · Medium · Top K Frequent Elements  (SOLUTION)

Bucket sort by frequency: buckets[f] holds every value seen exactly f times.
Frequencies are at most n, so walk buckets from high to low collecting values.
Sorting each (small) bucket enforces the smaller-value tie-break.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts: dict[int, int] = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1

    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)

    result: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in sorted(buckets[freq]):
            result.append(value)
            if len(result) == k:
                return result
    return result
