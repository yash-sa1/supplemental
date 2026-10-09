"""
Task 03 · Easy · Binary Search  (LeetCode #704)

Given a sequence `arr` sorted in ascending order and a `target`, return an
index where target is found, or -1 if it isn't there. If the target appears
more than once, any matching index is fine.

Write it twice:
    binary_search            -> iterative (a while loop with lo/hi)
    binary_search_recursive  -> recursive (you may add a helper function)

Don't slice the array (arr[lo:hi] copies = O(n)); pass indices around.
The tests use an instrumented array that counts every arr[i] read, so a
linear scan will be caught.

Example 1:
    Input:  arr = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4

Example 2:
    Input:  arr = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1

Constraints:
    - 0 <= len(arr) <= 10^6
    - arr is sorted ascending.

Target: O(log n) time. Iterative: O(1) space. Recursive: O(log n) space (call stack).
"""
from collections.abc import Sequence


def binary_search(arr: Sequence[int], target: int) -> int:
    raise NotImplementedError


def binary_search_recursive(arr: Sequence[int], target: int) -> int:
    raise NotImplementedError
