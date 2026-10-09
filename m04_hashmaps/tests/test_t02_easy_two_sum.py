import random

from common.loader import load_task

task = load_task(__file__)


def brute(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def test_example_1():
    assert task.two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    assert task.two_sum([3, 2, 4], 6) == [1, 2]


def test_example_3_duplicates():
    assert task.two_sum([3, 3], 6) == [0, 1]


def test_cannot_use_same_element_twice():
    assert task.two_sum([3, 5], 6) == []
    assert task.two_sum([4], 8) == []


def test_empty():
    assert task.two_sum([], 5) == []


def test_no_solution():
    assert task.two_sum([1, 2, 3], 100) == []


def test_negatives_and_zero():
    assert task.two_sum([-3, 4, 3, 90], 0) == [0, 2]
    assert task.two_sum([0, 4, 3, 0], 0) == [0, 3]


def test_earliest_completed_pair():
    # both (0,3) and (1,2) sum to 5; (1,2) completes first (j=2)
    assert task.two_sum([1, 2, 3, 4], 5) == [1, 2]


def test_earliest_first_index_for_ties():
    assert task.two_sum([2, 2, 2, 4], 6) == [0, 3]


def test_does_not_mutate_input():
    nums = [3, 2, 4]
    task.two_sum(nums, 6)
    assert nums == [3, 2, 4]


def test_randomized_against_brute_force():
    rng = random.Random(1)
    for _ in range(500):
        nums = [rng.randint(-10, 10) for _ in range(rng.randint(0, 12))]
        target = rng.randint(-15, 15)
        assert task.two_sum(nums, target) == brute(nums, target), f"nums={nums}, target={target}"


def test_large_input_answer_at_the_end():
    n = 100_000
    nums = list(range(0, 2 * n, 2)) + [-1, -3]  # only the last two can make -4
    target = -4
    assert task.two_sum(nums, target) == [n, n + 1]
