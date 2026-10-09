import pytest

from common.loader import load_task
from m02_linked_lists.framework import from_list, nodes_of, to_list

task = load_task(__file__)


def middle_index(n):
    return n // 2


def test_example_odd():
    head = from_list([1, 2, 3, 4, 5])
    assert task.middle_node(head).val == 3


def test_example_even_returns_second_middle():
    head = from_list([1, 2, 3, 4, 5, 6])
    assert task.middle_node(head).val == 4


def test_single_node():
    head = from_list([42])
    assert task.middle_node(head) is head


def test_two_nodes():
    head = from_list([1, 2])
    assert task.middle_node(head) is head.next


def test_three_nodes():
    head = from_list([1, 2, 3])
    assert task.middle_node(head) is head.next


def test_returns_the_node_object_not_a_copy():
    head = from_list([1, 2, 3])
    assert task.middle_node(head) is nodes_of(head)[1]


def test_duplicate_values_returns_correct_node():
    head = from_list([7, 7, 7, 7])
    assert task.middle_node(head) is nodes_of(head)[2]


@pytest.mark.parametrize("n", range(1, 25))
def test_many_sizes(n):
    head = from_list(range(n))
    nodes = nodes_of(head)
    assert task.middle_node(head) is nodes[middle_index(n)], f"n={n}"


def test_does_not_modify_list():
    head = from_list([1, 2, 3, 4])
    task.middle_node(head)
    assert to_list(head) == [1, 2, 3, 4]


def test_long_list():
    head = from_list(range(100_001))
    assert task.middle_node(head).val == 50_000
