"""
Task 10 · Hard · Merge k Sorted Lists  (SOLUTION)

Min-heap of the current front node of each list. Pop the smallest, append it,
push its successor. The heap never holds more than k items -> O(log k) per node.

The index `i` in each tuple is a tiebreaker: when two values are equal Python
would otherwise compare ListNode objects, which raises TypeError.
"""
import heapq
from typing import Optional

from m02_linked_lists.framework import ListNode


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node is not None]
    heapq.heapify(heap)
    dummy = ListNode()
    tail = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, i, node.next))
    tail.next = None
    return dummy.next
