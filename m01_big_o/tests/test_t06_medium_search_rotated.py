import math

import pytest

from common.loader import load_task
from common.probes import ProbeArray

task = load_task(__file__)


def search(values, target):
    return task.search_rotated(ProbeArray(values), target)


def rotate(values, k):
    return values[k:] + values[:k]


def test_example_1():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example_2_missing():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_example_3_single_missing():
    assert search([1], 0) == -1


def test_single_found():
    assert search([1], 1) == 0


def test_empty():
    assert search([], 1) == -1


def test_not_rotated():
    assert search([1, 2, 3, 4, 5], 4) == 3


def test_two_elements_rotated():
    assert search([3, 1], 1) == 1
    assert search([3, 1], 3) == 0
    assert search([3, 1], 2) == -1


def test_rotated_by_one():
    assert search([7, 1, 2, 3, 4, 5, 6], 7) == 0
    assert search([7, 1, 2, 3, 4, 5, 6], 6) == 6


def test_rotated_by_n_minus_one():
    assert search([2, 3, 4, 5, 6, 7, 1], 1) == 6


def test_target_is_the_pivot():
    assert search([5, 6, 1, 2, 3, 4], 1) == 2


def test_negatives():
    assert search([0, 5, -10, -7, -3], -7) == 3


@pytest.mark.parametrize("n", range(1, 13))
def test_every_rotation_every_value(n):
    base = list(range(0, 2 * n, 2))
    for k in range(n):
        values = rotate(base, k)
        for i, v in enumerate(values):
            assert search(values, v) == i, f"arr={values}, target={v}"
        for missing in range(-1, 2 * n + 1, 2):
            assert search(values, missing) == -1, f"arr={values}, target={missing}"


@pytest.mark.parametrize("k", [0, 1, 333_333, 500_000, 999_999])
@pytest.mark.parametrize("target_pos", [0, 1, 123_456, 999_998, 999_999])
def test_logarithmic_reads(k, target_pos):
    n = 1_000_000
    values = rotate(list(range(n)), k)
    arr = ProbeArray(values)
    target = values[target_pos]
    assert task.search_rotated(arr, target) == target_pos
    limit = 6 * (math.floor(math.log2(n)) + 2)
    assert arr.reads <= limit, f"Read {arr.reads} elements (limit {limit}); needs O(log n)"
