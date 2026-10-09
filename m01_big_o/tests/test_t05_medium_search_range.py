import bisect
import math
import random

import pytest

from common.loader import load_task
from common.probes import ProbeArray

task = load_task(__file__)


def search(values, target):
    return list(task.search_range(ProbeArray(values), target))


def expected(values, target):
    lo = bisect.bisect_left(values, target)
    hi = bisect.bisect_right(values, target) - 1
    return [lo, hi] if lo <= hi else [-1, -1]


def test_example_1():
    assert search([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_example_2_missing():
    assert search([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_example_3_empty():
    assert search([], 0) == [-1, -1]


def test_single_found():
    assert search([1], 1) == [0, 0]


def test_single_missing():
    assert search([1], 2) == [-1, -1]


def test_no_duplicates_first_equals_last():
    assert search([1, 2, 3, 4, 5], 3) == [2, 2]


def test_run_at_start():
    assert search([2, 2, 2, 3, 4], 2) == [0, 2]


def test_run_at_end():
    assert search([1, 2, 4, 4, 4], 4) == [2, 4]


def test_whole_array_is_target():
    assert search([6, 6, 6, 6], 6) == [0, 3]


def test_target_outside_range():
    assert search([3, 4, 5], 1) == [-1, -1]
    assert search([3, 4, 5], 9) == [-1, -1]


def test_negatives():
    assert search([-5, -5, -2, 0, 0, 0, 3], 0) == [3, 5]
    assert search([-5, -5, -2, 0, 0, 0, 3], -5) == [0, 1]


def test_randomized_against_bisect():
    rng = random.Random(34)
    for _ in range(300):
        values = sorted(rng.randint(-5, 5) for _ in range(rng.randint(0, 25)))
        target = rng.randint(-7, 7)
        assert search(values, target) == expected(values, target), f"arr={values}, target={target}"


def test_logarithmic_even_when_everything_matches():
    n = 1_000_000
    arr = ProbeArray([42] * n)
    assert list(task.search_range(arr, 42)) == [0, n - 1]
    limit = 4 * (math.floor(math.log2(n)) + 2)
    assert arr.reads <= limit, (
        f"Read {arr.reads} elements (limit {limit}). Walking outwards from a match is O(n); "
        "use a binary search for each edge instead."
    )


@pytest.mark.parametrize("target", [-1, 0, 250_000, 999_999, 1_000_000])
def test_logarithmic_reads(target):
    n = 1_000_000
    values = [i // 4 for i in range(n)]  # each value repeated 4 times
    arr = ProbeArray(values)
    assert list(task.search_range(arr, target)) == expected(values, target)
    assert arr.reads <= 4 * (math.floor(math.log2(n)) + 2)
