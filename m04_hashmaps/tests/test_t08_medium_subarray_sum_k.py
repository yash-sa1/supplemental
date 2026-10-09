import random

from common.loader import load_task

task = load_task(__file__)


def brute(nums, k):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            count += total == k
    return count


def test_example_1():
    assert task.subarray_sum([1, 1, 1], 2) == 2


def test_example_2():
    assert task.subarray_sum([1, 2, 3], 3) == 2


def test_empty():
    assert task.subarray_sum([], 0) == 0


def test_single_match():
    assert task.subarray_sum([5], 5) == 1


def test_single_no_match():
    assert task.subarray_sum([5], 3) == 0


def test_whole_array():
    assert task.subarray_sum([1, 2, 3, 4], 10) == 1


def test_negatives():
    assert task.subarray_sum([1, -1, 1, -1], 0) == 4


def test_zeros_many_subarrays():
    # every one of the n(n+1)/2 subarrays sums to 0
    assert task.subarray_sum([0, 0, 0, 0], 0) == 10


def test_negative_k():
    assert task.subarray_sum([-1, -1, 1], -2) == 1


def test_k_zero_is_not_counting_empty_subarray():
    assert task.subarray_sum([1, 2], 0) == 0


def test_sliding_window_does_not_work_with_negatives():
    assert task.subarray_sum([3, 4, -7, 1, 3, 3, 1, -4], 7) == 4


def test_randomized_against_brute_force():
    rng = random.Random(560)
    for _ in range(400):
        nums = [rng.randint(-3, 3) for _ in range(rng.randint(0, 15))]
        k = rng.randint(-4, 4)
        assert task.subarray_sum(nums, k) == brute(nums, k), f"nums={nums}, k={k}"


def test_large_input():
    n = 100_000
    assert task.subarray_sum([1] * n, 50_000) == n - 50_000 + 1
