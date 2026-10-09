"""
Task 10 · Hard · Merge k Sorted Lists  (LeetCode #23)

You're given a list of k linked lists, each sorted ascending. Merge them all
into one sorted linked list (reusing the nodes) and return its head.

Merging them one after another into a growing result is O(k * N) and will
time out on the big test (N = total nodes). Get it to O(N log k).
You may use the `heapq` module.

Example 1:
    Input:  [1 -> 4 -> 5,  1 -> 3 -> 4,  2 -> 6]
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Example 2:
    Input:  []
    Output: None

Example 3:
    Input:  [None]
    Output: None

Constraints:
    - 0 <= k <= 10^4
    - 0 <= total nodes N <= 2 * 10^5

Target: O(N log k) time.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    raise NotImplementedError
