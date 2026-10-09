"""
Task 03 · Easy · Reverse Linked List  (LeetCode #206)

Given the head of a singly linked list, reverse it IN PLACE (re-point the
existing nodes' .next; don't create new nodes or swap .val) and return the new head.

Write it twice:
    reverse_list            -> iterative, O(1) extra space
    reverse_list_recursive  -> recursive, O(n) space (call stack)

Example 1:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Example 2:
    Input:  None  (empty list)
    Output: None

Constraints:
    - 0 <= number of nodes <= 5000

Target: O(n) time.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    raise NotImplementedError


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    raise NotImplementedError
