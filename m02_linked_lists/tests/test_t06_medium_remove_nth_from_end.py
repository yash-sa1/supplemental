import pytest

from common.loader import load_task
from m02_linked_lists.framework import from_list, nodes_of, to_list

task = load_task(__file__)


def remove(values, n):
    return to_list(task.remove_nth_from_end(from_list(values), n))


def test_example_1():
    assert remove([1, 2, 3, 4, 5], 2) == [1, 2, 3, 5]


def test_example_2_only_node():
    assert task.remove_nth_from_end(from_list([1]), 1) is None


def test_example_3_remove_last():
    assert remove([1, 2], 1) == [1]


def test_remove_head():
    assert remove([1, 2], 2) == [2]
    assert remove([1, 2, 3, 4, 5], 5) == [2, 3, 4, 5]


def test_remove_last_of_many():
    assert remove([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4]


def test_duplicate_values_removes_by_position():
    head = from_list([7, 7, 7])
    nodes = nodes_of(head)
    result = task.remove_nth_from_end(head, 2)
    assert nodes_of(result) == [nodes[0], nodes[2]]


@pytest.mark.parametrize("length", range(1, 12))
def test_every_position(length):
    values = list(range(length))
    for n in range(1, length + 1):
        expected = values[: length - n] + values[length - n + 1 :]
        assert remove(values, n) == expected, f"values={values}, n={n}"


def test_keeps_remaining_nodes():
    head = from_list([1, 2, 3])
    nodes = nodes_of(head)
    result = task.remove_nth_from_end(head, 2)
    assert nodes_of(result) == [nodes[0], nodes[2]], "unlink the node; don't rebuild the list"


def test_long_list():
    n = 100_000
    assert remove(list(range(n)), n // 2)[: 3] == [0, 1, 2]
