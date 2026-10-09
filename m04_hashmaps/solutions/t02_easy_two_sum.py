"""
Task 02 · Easy · Two Sum  (SOLUTION)

For each number, ask "have I already seen target - x?" in O(1) via a dict of
value -> first index. Check BEFORE inserting so an element can't pair with itself.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    first_index: dict[int, int] = {}
    for j, x in enumerate(nums):
        need = target - x
        if need in first_index:
            return [first_index[need], j]
        if x not in first_index:  # keep the EARLIEST index for ties
            first_index[x] = j
    return []
