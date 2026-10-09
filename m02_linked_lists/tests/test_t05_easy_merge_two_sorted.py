import random

from common.loader import load_task
from m02_linked_lists.framework import from_list, nodes_of, to_list

task = load_task(__file__)


def merge(a, b):
    return to_list(task.merge_two_lists(from_list(a), from_list(b)))


def test_example_1():
    assert merge([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]


def test_example_2_first_empty():
    assert merge([], [0]) == [0]


def test_second_empty():
    assert merge([1, 2], []) == [1, 2]


def test_both_empty():
    assert task.merge_two_lists(None, None) is None


def test_all_of_first_smaller():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_all_of_second_smaller():
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


def test_different_lengths():
    assert merge([5], [1, 2, 3, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_negatives_and_duplicates():
    assert merge([-3, -3, 0], [-3, 0, 0, 2]) == [-3, -3, -3, 0, 0, 0, 2]


def test_splices_existing_nodes():
    a, b = from_list([1, 3, 5]), from_list([2, 4, 6])
    original = set(map(id, nodes_of(a) + nodes_of(b)))
    result = task.merge_two_lists(a, b)
    assert set(map(id, nodes_of(result))) == original, "reuse the input nodes; don't create new ones"


def test_stable_on_ties():
    a, b = from_list([1, 2]), from_list([1, 2])
    a_nodes, b_nodes = nodes_of(a), nodes_of(b)
    result = nodes_of(task.merge_two_lists(a, b))
    assert result == [a_nodes[0], b_nodes[0], a_nodes[1], b_nodes[1]], "on a tie, list1's node goes first"


def test_randomized():
    rng = random.Random(21)
    for _ in range(300):
        a = sorted(rng.randint(-10, 10) for _ in range(rng.randint(0, 10)))
        b = sorted(rng.randint(-10, 10) for _ in range(rng.randint(0, 10)))
        assert merge(a, b) == sorted(a + b), f"a={a}, b={b}"


def test_long_lists():
    a = list(range(0, 200_000, 2))
    b = list(range(1, 200_000, 2))
    assert merge(a, b) == list(range(200_000))
