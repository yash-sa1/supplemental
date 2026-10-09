"""
Task 06 · Medium · Remove Nth Node From End of List  (LeetCode #19)

Given the head of a singly linked list, remove the n-th node from the END
(n = 1 means the last node) and return the head of the resulting list.

Do it in ONE pass (don't count the length first).

Example 1:
    Input:  head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

Example 2:
    Input:  head = 1, n = 1
    Output: None

Example 3:
    Input:  head = 1 -> 2, n = 1
    Output: 1

Constraints:
    - 1 <= number of nodes <= 10^5
    - 1 <= n <= number of nodes

Target: O(length) time, one pass, O(1) space.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def remove_nth_from_end(head: ListNode, n: int) -> Optional[ListNode]:
    raise NotImplementedError
