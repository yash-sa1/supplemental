"""
Task 05 · Easy · Merge Two Sorted Lists  (LeetCode #21)

Given the heads of two sorted (ascending) singly linked lists, merge them
into one sorted list by SPLICING the existing nodes together, and return
its head. Don't create new value-holding nodes (a throwaway dummy node is fine).

When values are equal, nodes from list1 should come first (stable merge).

Example 1:
    Input:  list1 = 1 -> 2 -> 4,  list2 = 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Example 2:
    Input:  list1 = None, list2 = 0
    Output: 0

Constraints:
    - 0 <= nodes in each list <= 10^5
    - Both lists are sorted ascending.

Target: O(m + n) time, O(1) extra space.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    raise NotImplementedError
