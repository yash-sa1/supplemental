"""
Task 09 · Hard · Reverse Nodes in k-Group  (LeetCode #25)

Given the head of a linked list, reverse the nodes k at a time and return the
new head. If the number of nodes left at the end is less than k, leave that
last chunk as it is.

Re-link the nodes themselves — don't swap values, don't build a new list.

Example 1:
    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 2 -> 1 -> 4 -> 3 -> 5

Example 2:
    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 3
    Output: 3 -> 2 -> 1 -> 4 -> 5

Constraints:
    - 0 <= number of nodes <= 10^5
    - 1 <= k

Target: O(n) time, O(1) extra space.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    raise NotImplementedError
