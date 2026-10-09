import pytest

from common.loader import load_task
from m02_linked_lists.framework import from_list, nodes_of, to_list

task = load_task(__file__)


def expected(values, k):
    out = []
    for i in range(0, len(values), k):
        chunk = values[i : i + k]
        out.extend(reversed(chunk) if len(chunk) == k else chunk)
    return out


def run(values, k):
    return to_list(task.reverse_k_group(from_list(values), k))


def test_example_1():
    assert run([1, 2, 3, 4, 5], 2) == [2, 1, 4, 3, 5]


def test_example_2():
    assert run([1, 2, 3, 4, 5], 3) == [3, 2, 1, 4, 5]


def test_empty():
    assert task.reverse_k_group(None, 2) is None


def test_k_equals_one_is_unchanged():
    assert run([1, 2, 3], 1) == [1, 2, 3]


def test_k_equals_length_reverses_all():
    assert run([1, 2, 3, 4], 4) == [4, 3, 2, 1]


def test_k_greater_than_length_is_unchanged():
    assert run([1, 2, 3], 5) == [1, 2, 3]


def test_exact_multiple_of_k():
    assert run([1, 2, 3, 4, 5, 6], 3) == [3, 2, 1, 6, 5, 4]


def test_single_node():
    assert run([1], 2) == [1]


@pytest.mark.parametrize("length", range(0, 13))
def test_all_lengths_and_ks(length):
    values = list(range(length))
    for k in range(1, length + 2):
        assert run(values, k) == expected(values, k), f"values={values}, k={k}"


def test_relinks_nodes_instead_of_swapping_values():
    head = from_list([1, 2, 3, 4, 5])
    by_val = {node.val: node for node in nodes_of(head)}
    result = nodes_of(task.reverse_k_group(head, 2))
    assert [node.val for node in result] == [2, 1, 4, 3, 5]
    assert all(node is by_val[node.val] for node in result), "don't swap .val; move the nodes"


def test_long_list():
    n = 100_000
    assert run(list(range(n)), 7) == expected(list(range(n)), 7)
