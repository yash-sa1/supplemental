"""
Task 03 · Easy · Reverse Linked List  (SOLUTION)
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr is not None:
        nxt = curr.next   # 1. save the rest of the list
        curr.next = prev  # 2. flip the pointer
        prev = curr       # 3. advance both
        curr = nxt
    return prev  # curr fell off the end; prev is the old tail = new head


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)  # reverse everything after head
    head.next.next = head  # the node after head now points back at head
    head.next = None       # head becomes the tail
    return new_head
