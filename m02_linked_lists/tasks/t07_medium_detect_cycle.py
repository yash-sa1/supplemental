"""
Task 07 · Medium · Linked List Cycle  (LeetCode #141 + #142)

A list has a cycle if following .next eventually revisits a node.

    has_cycle(head)    -> True/False
    detect_cycle(head) -> the NODE where the cycle begins, or None if no cycle

Don't modify the list. Aim for O(1) extra space (no set of visited nodes):
Floyd's tortoise-and-hare algorithm.

Example 1:
    Input:  3 -> 2 -> 0 -> -4
                 ^          |
                 +----------+      (-4 points back to 2)
    has_cycle:    True
    detect_cycle: the node with value 2

Example 2:
    Input:  1 -> 2 -> None
    has_cycle:    False
    detect_cycle: None

Constraints:
    - 0 <= number of nodes <= 10^5

Target: O(n) time, O(1) space.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    raise NotImplementedError


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    raise NotImplementedError
