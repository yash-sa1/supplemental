"""
Task 04 · Easy · Middle of the Linked List  (LeetCode #876)

Given the head of a non-empty singly linked list, return the MIDDLE NODE
(the node object, not its value). If there are two middle nodes, return the
SECOND one. Don't modify the list.

Do it in ONE pass without counting the length first.

Example 1:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: the node with value 3

Example 2:
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6
    Output: the node with value 4   (second of the two middles: 3 and 4)

Constraints:
    - 1 <= number of nodes <= 10^5

Target: O(n) time, O(1) space.
"""
from m02_linked_lists.framework import ListNode


def middle_node(head: ListNode) -> ListNode:
    raise NotImplementedError
