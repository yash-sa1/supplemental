import functools
import random

from common.loader import load_task

task = load_task(__file__)


def brute_force(nums, k):
    """Try every way of placing the cuts (fine for tiny inputs)."""
    n = len(nums)
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)

    @functools.cache
    def best(start, pieces):
        if pieces == 1:
            return prefix[n] - prefix[start]
        result = float("inf")
        for end in range(start + 1, n - pieces + 2):
            first = prefix[end] - prefix[start]
            result = min(result, max(first, best(end, pieces - 1)))
        return result

    return best(0, k)


def test_example_1():
    assert task.split_array([7, 2, 5, 10, 8], 2) == 18


def test_example_2():
    assert task.split_array([1, 2, 3, 4, 5], 2) == 9


def test_k_equals_one_is_total():
    assert task.split_array([1, 4, 4], 1) == 9


def test_k_equals_n_is_max():
    assert task.split_array([1, 4, 4], 3) == 4


def test_single_element():
    assert task.split_array([10], 1) == 10


def test_all_zeros():
    assert task.split_array([0, 0, 0, 0], 2) == 0


def test_zeros_mixed_in():
    assert task.split_array([0, 5, 0, 5, 0], 2) == 5


def test_one_giant_element():
    assert task.split_array([1, 1, 100, 1, 1], 2) == 102
    assert task.split_array([1, 1, 100, 1, 1], 3) == 100


def test_all_equal():
    assert task.split_array([3] * 9, 3) == 9


def test_does_not_mutate_input():
    nums = [7, 2, 5, 10, 8]
    task.split_array(nums, 2)
    assert nums == [7, 2, 5, 10, 8]


def test_randomized_against_brute_force():
    rng = random.Random(410)
    for _ in range(300):
        n = rng.randint(1, 9)
        nums = [rng.randint(0, 20) for _ in range(n)]
        k = rng.randint(1, n)
        assert task.split_array(nums, k) == brute_force(nums, k), f"nums={nums}, k={k}"


def test_large_input_is_fast():
    rng = random.Random(4100)
    nums = [rng.randint(0, 10**6) for _ in range(10_000)]
    result = task.split_array(nums, 50)
    # sanity: must be between the obvious bounds
    assert max(nums) <= result <= sum(nums)
    # and it must actually be achievable with 50 pieces but not with a cap of result - 1
    def pieces(cap):
        count, cur = 1, 0
        for x in nums:
            if cur + x > cap:
                count, cur = count + 1, x
            else:
                cur += x
        return count

    assert pieces(result) <= 50
    assert result == max(nums) or pieces(result - 1) > 50
