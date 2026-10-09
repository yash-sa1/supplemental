"""
Task 07 · Medium · Linked List Cycle  (SOLUTION)

Floyd: slow moves 1, fast moves 2. If there's a cycle, fast laps slow and
they meet inside it. Then, a pointer from head and a pointer from the meeting
point, both moving 1 step, meet exactly at the cycle's start.
(Why: if the tail before the cycle has length a, the meeting point is a steps
short of the cycle start, going around the loop.)
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def _meeting_point(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:  # `is`, not `==`: same node object
            return slow
    return None


def has_cycle(head: Optional[ListNode]) -> bool:
    return _meeting_point(head) is not None


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    meet = _meeting_point(head)
    if meet is None:
        return None
    a, b = head, meet
    while a is not b:
        a = a.next
        b = b.next
    return a
