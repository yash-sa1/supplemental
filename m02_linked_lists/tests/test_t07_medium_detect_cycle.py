import pytest

from common.loader import load_task
from m02_linked_lists.framework import ListNode, from_list, nodes_of, to_list

task = load_task(__file__)


def build(values, pos):
    """Build a list; if pos >= 0 the last node links back to the node at index pos."""
    head = from_list(values)
    if head is None or pos < 0:
        return head, None
    nodes = nodes_of(head)
    nodes[-1].next = nodes[pos]
    return head, nodes[pos]


def snapshot(head, count):
    """Record every node's .next so we can check nothing was modified."""
    links, node = [], head
    for _ in range(count):
        if node is None:
            break
        links.append((node, node.next, node.val))
        node = node.next
    return links


def test_example_1():
    head, start = build([3, 2, 0, -4], 1)
    assert task.has_cycle(head) is True
    assert task.detect_cycle(head) is start


def test_example_2_no_cycle():
    head, _ = build([1, 2], -1)
    assert task.has_cycle(head) is False
    assert task.detect_cycle(head) is None


def test_empty():
    assert task.has_cycle(None) is False
    assert task.detect_cycle(None) is None


def test_single_node_no_cycle():
    head = ListNode(1)
    assert task.has_cycle(head) is False
    assert task.detect_cycle(head) is None


def test_single_node_self_loop():
    head = ListNode(1)
    head.next = head
    assert task.has_cycle(head) is True
    assert task.detect_cycle(head) is head


def test_two_nodes_cycle_to_head():
    head, start = build([1, 2], 0)
    assert task.has_cycle(head) is True
    assert task.detect_cycle(head) is start


def test_two_nodes_self_loop_on_tail():
    head, start = build([1, 2], 1)
    assert task.detect_cycle(head) is start


def test_whole_list_is_cycle():
    head, start = build(list(range(10)), 0)
    assert task.detect_cycle(head) is head


def test_duplicate_values_must_compare_nodes_not_values():
    # every value is the same: comparing .val instead of node identity gives wrong answers
    head, start = build([5] * 8, 5)
    assert task.detect_cycle(head) is start
    no_cycle, _ = build([5] * 8, -1)
    assert task.has_cycle(no_cycle) is False


@pytest.mark.parametrize("length", range(1, 15))
def test_every_cycle_position(length):
    values = list(range(length))
    for pos in range(-1, length):
        head, start = build(values, pos)
        assert task.has_cycle(head) is (pos >= 0), f"len={length}, pos={pos}"
        assert task.detect_cycle(head) is start, f"len={length}, pos={pos}"


def test_does_not_modify_list_with_cycle():
    head, _ = build(list(range(6)), 2)
    before = snapshot(head, 6)
    task.has_cycle(head)
    task.detect_cycle(head)
    assert snapshot(head, 6) == before, "don't change .next or .val while searching"


def test_does_not_modify_list_without_cycle():
    head, _ = build([1, 2, 3], -1)
    task.detect_cycle(head)
    assert to_list(head) == [1, 2, 3]


def test_long_list_with_long_cycle():
    n = 100_000
    head, start = build(list(range(n)), 30_000)
    assert task.detect_cycle(head) is start
