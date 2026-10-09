import math

import pytest

from common.loader import load_task
from common.probes import ProbeArray

task = load_task(__file__)

# Every test runs against both versions.
IMPLS = ["binary_search", "binary_search_recursive"]


@pytest.fixture(params=IMPLS)
def search(request):
    fn = getattr(task, request.param)
    return lambda values, target: fn(ProbeArray(values), target)


def test_example_found(search):
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_example_not_found(search):
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_empty(search):
    assert search([], 5) == -1


def test_single_found(search):
    assert search([5], 5) == 0


def test_single_not_found_smaller(search):
    assert search([5], 1) == -1


def test_single_not_found_larger(search):
    assert search([5], 9) == -1


def test_two_elements(search):
    assert search([1, 3], 1) == 0
    assert search([1, 3], 3) == 1
    assert search([1, 3], 2) == -1
    assert search([1, 3], 0) == -1
    assert search([1, 3], 4) == -1


def test_first_and_last(search):
    arr = [2, 4, 6, 8, 10, 12, 14]
    assert search(arr, 2) == 0
    assert search(arr, 14) == 6


def test_target_below_all(search):
    assert search([10, 20, 30], -100) == -1


def test_target_above_all(search):
    assert search([10, 20, 30], 100) == -1


def test_negative_numbers(search):
    assert search([-50, -20, -3, -1], -20) == 1


def test_duplicates_return_a_matching_index(search):
    values = [1, 2, 2, 2, 2, 3]
    i = search(values, 2)
    assert i != -1 and values[i] == 2


def test_all_same(search):
    values = [7] * 10
    assert values[search(values, 7)] == 7
    assert search(values, 8) == -1


@pytest.mark.parametrize("n", range(0, 18))
def test_every_element_every_size(search, n):
    """Off-by-one hunter: every present value and every gap, for many sizes (odd and even)."""
    values = list(range(0, 2 * n, 2))  # 0, 2, 4, ...
    for i, v in enumerate(values):
        assert search(values, v) == i, f"n={n}: couldn't find {v} at index {i}"
    for missing in range(-1, 2 * n + 1, 2):  # -1, 1, 3, ... (all gaps + both ends)
        assert search(values, missing) == -1, f"n={n}: found missing value {missing}"


@pytest.mark.parametrize("impl", IMPLS)
@pytest.mark.parametrize("target", [0, 123_456, 999_999, -5, 2_000_000, 500_001])
def test_logarithmic_reads(impl, target):
    n = 1_000_000
    arr = ProbeArray(range(0, 2 * n, 2))  # even numbers only; odd targets are missing
    expected = target // 2 if 0 <= target < 2 * n and target % 2 == 0 else -1
    assert getattr(task, impl)(arr, target) == expected
    limit = 2 * (math.floor(math.log2(n)) + 2)
    assert arr.reads <= limit, (
        f"Read {arr.reads} elements of a 1,000,000 element array; "
        f"binary search needs ~{math.ceil(math.log2(n))} (limit {limit})"
    )


@pytest.mark.parametrize("impl", IMPLS)
def test_does_not_slice(impl):
    """Slicing copies the array; ProbeArray raises TypeError if you try."""
    arr = ProbeArray(range(100))
    getattr(task, impl)(arr, 73)  # would raise TypeError on a slice
