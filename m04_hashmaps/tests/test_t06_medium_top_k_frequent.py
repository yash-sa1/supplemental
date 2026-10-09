import random
from collections import Counter

from common.loader import load_task

task = load_task(__file__)


def expected(nums, k):
    counts = Counter(nums)
    ranked = sorted(counts, key=lambda v: (-counts[v], v))
    return sorted(ranked[:k])


def run(nums, k):
    return sorted(task.top_k_frequent(nums, k))


def test_example_1():
    assert run([1, 1, 1, 2, 2, 3], 2) == [1, 2]


def test_example_2():
    assert run([1], 1) == [1]


def test_k_equals_distinct_count():
    assert run([4, 4, 5, 6], 3) == [4, 5, 6]


def test_all_unique_tie_prefers_smaller():
    assert run([5, 3, 9, 1], 2) == [1, 3]


def test_tie_at_cutoff():
    assert run([7, 7, 2, 2, 9, 9, 1], 2) == [2, 7]


def test_negatives():
    assert run([-1, -1, -2, -2, -2, 3], 1) == [-2]


def test_most_frequent_not_first():
    assert run([1, 2, 3, 3, 3, 3], 1) == [3]


def test_returns_exactly_k():
    assert len(task.top_k_frequent([1, 1, 2, 2, 3, 3, 4], 3)) == 3


def test_does_not_mutate_input():
    nums = [3, 1, 1, 2]
    task.top_k_frequent(nums, 1)
    assert nums == [3, 1, 1, 2]


def test_randomized():
    rng = random.Random(347)
    for _ in range(400):
        nums = [rng.randint(-5, 5) for _ in range(rng.randint(1, 25))]
        k = rng.randint(1, len(set(nums)))
        assert run(nums, k) == expected(nums, k), f"nums={nums}, k={k}"


def test_large_input():
    rng = random.Random(3470)
    nums = [rng.randint(0, 5000) for _ in range(100_000)] + [123] * 500 + [77] * 400
    assert run(nums, 2) == [77, 123]
