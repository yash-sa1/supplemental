"""
Task 05 · Easy · Merge Two Sorted Lists  (SOLUTION)

Dummy-head pattern: a placeholder node means the "first node" isn't a
special case; append to `tail` and return dummy.next at the end.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:  # <= keeps it stable: list1 wins ties
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    tail.next = list1 if list1 is not None else list2  # attach the leftovers
    return dummy.next
