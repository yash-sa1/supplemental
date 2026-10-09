"""
Task 04 · Easy · Middle of the Linked List  (SOLUTION)

Fast/slow pointers: fast moves 2 steps for every 1 of slow, so when fast
runs off the end, slow is halfway.
"""
from m02_linked_lists.framework import ListNode


def middle_node(head: ListNode) -> ListNode:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
