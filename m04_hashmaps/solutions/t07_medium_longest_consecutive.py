"""
Task 07 · Medium · Longest Consecutive Sequence  (SOLUTION)

Put everything in a set. A number x starts a run only if x - 1 is absent;
from each start, walk x+1, x+2, ... Each number is walked over at most once
in total, so the whole thing is O(n) even though there's a nested loop.
"""


def longest_consecutive(nums: list[int]) -> int:
    values = set(nums)
    best = 0
    for x in values:  # iterate the set, not nums: skips duplicate starts
        if x - 1 in values:
            continue  # not the start of a run
        length = 1
        while x + length in values:
            length += 1
        best = max(best, length)
    return best
