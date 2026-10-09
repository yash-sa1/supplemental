"""
Task 06 · Medium · Remove Nth Node From End of List  (SOLUTION)

Gap technique: move `fast` n steps ahead, then move both until fast hits the
last node. `slow` is then just BEFORE the node to delete. A dummy node in
front handles "delete the head" with no special case.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def remove_nth_from_end(head: ListNode, n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next  # skip over the n-th from end
    return dummy.next
