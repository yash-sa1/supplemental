"""
Given building blocks for linked-list tasks. You don't need to edit this file.

    ListNode   - node of a singly linked list  (val, next)
    DListNode  - node of a doubly linked list  (val, prev, next)
    from_list  - [1, 2, 3] -> 1 -> 2 -> 3 -> None, returns the head
    to_list    - head -> [1, 2, 3]   (raises if it finds a cycle)
    nodes_of   - head -> [node1, node2, node3]  (the node objects themselves)

Handy in a REPL / debugger:
    >>> head = from_list([1, 2, 3])
    >>> head
    ListNode(1) -> ListNode(2) -> ListNode(3) -> None
"""
from collections.abc import Iterable
from typing import Any, Optional


class ListNode:
    def __init__(self, val: Any = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        parts, node, seen = [], self, set()
        while node is not None and id(node) not in seen and len(parts) < 20:
            seen.add(id(node))
            parts.append(f"ListNode({node.val!r})")
            node = node.next
        if node is None:
            parts.append("None")
        elif id(node) in seen:
            parts.append(f"(cycle back to ListNode({node.val!r}))")
        else:
            parts.append("...")
        return " -> ".join(parts)


class DListNode:
    def __init__(
        self,
        val: Any = 0,
        prev: Optional["DListNode"] = None,
        next: Optional["DListNode"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"DListNode({self.val!r})"


def from_list(values: Iterable) -> Optional[ListNode]:
    """Build a singly linked list and return its head (None for no values)."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def nodes_of(head: Optional[ListNode]) -> list[ListNode]:
    """Return the node objects in order. Raises ValueError if the list has a cycle."""
    nodes, seen = [], set()
    node = head
    while node is not None:
        if id(node) in seen:
            raise ValueError(
                f"Cycle detected: node with val={node.val!r} appears twice. "
                "Some .next pointer points backwards into the list."
            )
        seen.add(id(node))
        nodes.append(node)
        node = node.next
    return nodes


def to_list(head: Optional[ListNode]) -> list:
    """Return the values in order. Raises ValueError if the list has a cycle."""
    return [node.val for node in nodes_of(head)]
