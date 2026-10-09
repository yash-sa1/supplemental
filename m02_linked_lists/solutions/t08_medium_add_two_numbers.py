"""
Task 08 · Medium · Add Two Numbers  (SOLUTION)
"""
from m02_linked_lists.framework import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    carry = 0
    # keep going while either list has digits OR there's a carry left over
    while l1 is not None or l2 is not None or carry:
        total = carry
        if l1 is not None:
            total += l1.val
            l1 = l1.next
        if l2 is not None:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next
