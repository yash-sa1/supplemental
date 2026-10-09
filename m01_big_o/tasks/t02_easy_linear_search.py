"""
Task 02 · Easy · Linear Search

Given a sequence `arr` (NOT necessarily sorted) and a `target`, return the
index of the FIRST occurrence of target, or -1 if it isn't there.

Implement the search yourself: no `arr.index(...)`. (The tests pass an
instrumented array that only supports len(arr), arr[i] and iteration.)

Example 1:
    Input:  arr = [4, 2, 7, 2], target = 2
    Output: 1

Example 2:
    Input:  arr = [4, 2, 7], target = 5
    Output: -1

Constraints:
    - 0 <= len(arr) <= 10^6
    - Elements can be any type that supports ==.
    - Stop as soon as you find the target.

Target: O(n) time, O(1) extra space.
"""
from collections.abc import Sequence
from typing import Any


def linear_search(arr: Sequence, target: Any) -> int:
    raise NotImplementedError
