import pytest

from common.loader import load_task
from m02_linked_lists.framework import from_list, nodes_of, to_list

task = load_task(__file__)

IMPLS = ["reverse_list", "reverse_list_recursive"]


@pytest.fixture(params=IMPLS)
def reverse(request):
    return getattr(task, request.param)


def test_example(reverse):
    assert to_list(reverse(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]


def test_empty(reverse):
    assert reverse(None) is None


def test_single_node(reverse):
    head = from_list([1])
    result = reverse(head)
    assert result is head
    assert result.next is None


def test_two_nodes(reverse):
    assert to_list(reverse(from_list([1, 2]))) == [2, 1]


def test_duplicates(reverse):
    assert to_list(reverse(from_list([1, 1, 2, 2]))) == [2, 2, 1, 1]


def test_reverses_nodes_not_values(reverse):
    head = from_list([1, 2, 3])
    original = nodes_of(head)
    result = reverse(head)
    assert nodes_of(result) == original[::-1], (
        "Reuse the existing nodes: re-point .next instead of creating nodes / swapping .val"
    )
    assert [n.val for n in original] == [1, 2, 3], "don't change .val"


def test_old_head_becomes_tail(reverse):
    head = from_list([1, 2, 3])
    reverse(head)
    assert head.next is None, "the old head is now the tail; its .next must be None (else: cycle)"


def test_reverse_twice_is_identity(reverse):
    values = list(range(10))
    assert to_list(reverse(reverse(from_list(values)))) == values


def test_long_list(reverse):
    n = 800  # stays under Python's default recursion limit (1000) for the recursive version
    assert to_list(reverse(from_list(range(n)))) == list(range(n - 1, -1, -1))


def test_iterative_handles_very_long_list():
    n = 200_000  # too deep for recursion: the iterative version must handle it
    assert to_list(task.reverse_list(from_list(range(n))))[:3] == [n - 1, n - 2, n - 3]
