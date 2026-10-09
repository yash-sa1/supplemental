import random

from common.loader import load_task

task = load_task(__file__)


def brute(nums):
    s = sorted(set(nums))
    best = cur = 0
    for i, x in enumerate(s):
        cur = cur + 1 if i and x == s[i - 1] + 1 else 1
        best = max(best, cur)
    return best


def test_example_1():
    assert task.longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_example_2():
    assert task.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_empty():
    assert task.longest_consecutive([]) == 0


def test_single():
    assert task.longest_consecutive([5]) == 1


def test_all_duplicates():
    assert task.longest_consecutive([2, 2, 2]) == 1


def test_duplicates_inside_run():
    assert task.longest_consecutive([1, 2, 2, 3]) == 3


def test_no_consecutive():
    assert task.longest_consecutive([10, 30, 20]) == 1


def test_negatives_across_zero():
    assert task.longest_consecutive([-2, -1, 0, 1, 5]) == 4


def test_two_runs_picks_longer():
    assert task.longest_consecutive([1, 2, 3, 10, 11, 12, 13]) == 4


def test_extreme_values():
    assert task.longest_consecutive([-10**9, 10**9, 10**9 - 1]) == 2


def test_does_not_mutate_input():
    nums = [3, 1, 2]
    task.longest_consecutive(nums)
    assert nums == [3, 1, 2]


def test_randomized():
    rng = random.Random(128)
    for _ in range(400):
        nums = [rng.randint(-10, 10) for _ in range(rng.randint(0, 20))]
        assert task.longest_consecutive(nums) == brute(nums), f"nums={nums}"


def test_large_one_long_run():
    n = 100_000
    nums = list(range(n))
    random.Random(1280).shuffle(nums)
    assert task.longest_consecutive(nums) == n


def test_large_with_many_duplicates():
    # iterating over nums instead of the set re-walks the run for each duplicate start
    nums = [0] * 50_000 + list(range(50_000))
    assert task.longest_consecutive(nums) == 50_000
