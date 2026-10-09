import random

from common.loader import load_task
from m02_linked_lists.framework import from_list, nodes_of, to_list

task = load_task(__file__)


def merge(*lists):
    return to_list(task.merge_k_lists([from_list(values) for values in lists]))


def test_example_1():
    assert merge([1, 4, 5], [1, 3, 4], [2, 6]) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_example_2_no_lists():
    assert task.merge_k_lists([]) is None


def test_example_3_one_empty_list():
    assert task.merge_k_lists([None]) is None


def test_all_empty():
    assert task.merge_k_lists([None, None, None]) is None


def test_single_list():
    assert merge([1, 2, 3]) == [1, 2, 3]


def test_some_empty():
    assert merge([], [2], [], [1, 3], []) == [1, 2, 3]


def test_many_equal_values():
    # equal values across lists: a heap of (val, node) crashes comparing ListNodes
    assert merge([1, 1], [1, 1], [1]) == [1, 1, 1, 1, 1]


def test_negatives():
    assert merge([-10, -5, 0], [-7, 3], [-6]) == [-10, -7, -6, -5, 0, 3]


def test_reuses_nodes():
    lists = [from_list([1, 4]), from_list([2, 3])]
    original = {id(n) for head in lists for n in nodes_of(head)}
    result = task.merge_k_lists(lists)
    assert {id(n) for n in nodes_of(result)} == original, "reuse the input nodes"


def test_randomized():
    rng = random.Random(23)
    for _ in range(200):
        lists = [sorted(rng.randint(-20, 20) for _ in range(rng.randint(0, 6))) for _ in range(rng.randint(0, 6))]
        assert merge(*lists) == sorted(v for values in lists for v in values), f"lists={lists}"


def test_many_lists_is_fast():
    rng = random.Random(230)
    k, per_list = 5_000, 40  # N = 200,000; O(k*N) = 10^9 steps -> timeout
    lists = [sorted(rng.randint(0, 10**6) for _ in range(per_list)) for _ in range(k)]
    result = merge(*lists)
    assert len(result) == k * per_list
    assert result == sorted(result)
