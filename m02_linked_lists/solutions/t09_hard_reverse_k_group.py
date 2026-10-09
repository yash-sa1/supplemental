"""
Task 09 · Hard · Reverse Nodes in k-Group  (SOLUTION)

    dummy -> [a -> b -> c] -> [d -> e -> f] -> g
    group_prev ^

For each group: check k nodes exist, reverse them (classic prev/curr loop,
but starting prev at the node AFTER the group so the reversed group's tail
already points onward), then hook group_prev up to the new group head.
"""
from typing import Optional

from m02_linked_lists.framework import ListNode


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        # find the k-th node of this group; stop if fewer than k remain
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next
        group_next = kth.next

        # reverse the group
        prev, curr = group_next, group_prev.next
        while curr is not group_next:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

        # reconnect: old first node is now the group's last
        old_first = group_prev.next
        group_prev.next = kth
        group_prev = old_first
