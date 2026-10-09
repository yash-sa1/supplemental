import random

import pytest

from common.loader import load_task

task = load_task(__file__)


def brute(nums, k):
    return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]


def test_example_1():
    assert task.max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_example_2():
    assert task.max_sliding_window([1], 1) == [1]


def test_k_equals_one_is_identity():
    assert task.max_sliding_window([4, -2, 7], 1) == [4, -2, 7]


def test_k_equals_n_is_single_max():
    assert task.max_sliding_window([4, -2, 7, 1], 4) == [7]


def test_increasing():
    assert task.max_sliding_window([1, 2, 3, 4, 5], 2) == [2, 3, 4, 5]


def test_decreasing():
    # the max leaves the window every step: tests expiring the front
    assert task.max_sliding_window([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2]


def test_duplicates():
    assert task.max_sliding_window([7, 7, 7, 7], 2) == [7, 7, 7]
    assert task.max_sliding_window([1, 3, 3, 1, 1], 3) == [3, 3, 3]


def test_all_negative():
    assert task.max_sliding_window([-5, -1, -3, -4], 2) == [-1, -1, -3]


@pytest.mark.parametrize("k", [0, -1, 4])
def test_invalid_k(k):
    with pytest.raises(ValueError):
        task.max_sliding_window([1, 2, 3], k)


def test_empty_nums_raises():
    with pytest.raises(ValueError):
        task.max_sliding_window([], 1)


def test_does_not_mutate_input():
    nums = [1, 3, -1, -3, 5]
    task.max_sliding_window(nums, 2)
    assert nums == [1, 3, -1, -3, 5]


def test_randomized_against_brute_force():
    rng = random.Random(239)
    for _ in range(400):
        n = rng.randint(1, 20)
        nums = [rng.randint(-5, 5) for _ in range(n)]
        k = rng.randint(1, n)
        assert task.max_sliding_window(nums, k) == brute(nums, k), f"nums={nums}, k={k}"


def test_large_window_is_fast():
    rng = random.Random(2390)
    nums = [rng.randint(-10**4, 10**4) for _ in range(100_000)]
    k = 50_000  # O(n*k) = 2.5*10^9 steps
    result = task.max_sliding_window(nums, k)
    assert len(result) == len(nums) - k + 1
    assert result[0] == max(nums[:k])
    assert result[-1] == max(nums[-k:])
