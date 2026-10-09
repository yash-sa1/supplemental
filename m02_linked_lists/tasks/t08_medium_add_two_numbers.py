"""
Task 08 · Medium · Add Two Numbers  (LeetCode #2)

Two non-negative integers are stored as linked lists with digits in REVERSE
order (the head is the ones digit). Add them and return the sum as a linked
list in the same format. Don't modify the input lists.

Don't convert the whole list to a Python int and back — work digit by digit
with a carry, the way you'd add on paper.

Example 1:
    Input:  l1 = 2 -> 4 -> 3,  l2 = 5 -> 6 -> 4       (342 + 465)
    Output: 7 -> 0 -> 8                                 (807)

Example 2:
    Input:  l1 = 0,  l2 = 0
    Output: 0

Example 3:
    Input:  l1 = 9 -> 9 -> 9 -> 9,  l2 = 9 -> 9        (9999 + 99)
    Output: 8 -> 9 -> 0 -> 0 -> 1                       (10098)

Constraints:
    - 1 <= nodes in each list <= 10^5
    - 0 <= digit <= 9, no leading zeros except the number 0 itself.

Target: O(max(m, n)) time.
"""
from m02_linked_lists.framework import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    raise NotImplementedError
