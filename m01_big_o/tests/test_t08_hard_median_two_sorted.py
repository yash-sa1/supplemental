import math
import random
import statistics

import pytest

from common.loader import load_task
from common.probes import ProbeArray

task = load_task(__file__)


def median(a, b):
    return task.find_median_sorted_arrays(ProbeArray(a), ProbeArray(b))


def test_example_1_odd_total():
    assert median([1, 3], [2]) == 2.0


def test_example_2_even_total():
    assert median([1, 2], [3, 4]) == 2.5


def test_returns_float():
    result = median([1], [3])
    assert isinstance(result, float) and result == 2.0


def test_first_empty():
    assert median([], [1, 2, 3]) == 2.0
    assert median([], [1, 2, 3, 4]) == 2.5


def test_second_empty():
    assert median([5], []) == 5.0
    assert median([1, 2], []) == 1.5


def test_both_empty_raises():
    with pytest.raises(ValueError):
        median([], [])


def test_single_each():
    assert median([1], [2]) == 1.5


def test_all_of_a_before_b():
    assert median([1, 2, 3], [10, 11, 12, 13]) == 10.0


def test_interleaved():
    assert median([1, 3, 5, 7], [2, 4, 6, 8]) == 4.5


def test_very_different_sizes():
    assert median([100], list(range(1, 11))) == 6.0


def test_duplicates_across_arrays():
    assert median([1, 1, 1], [1, 1]) == 1.0
    assert median([1, 2, 2], [2, 2, 3]) == 2.0


def test_negatives():
    assert median([-5, -3, -1], [-4, -2]) == -3.0


def test_randomized_against_statistics_median():
    rng = random.Random(4)
    for _ in range(500):
        a = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0, 12)))
        b = sorted(rng.randint(-50, 50) for _ in range(rng.randint(0 if a else 1, 12)))
        assert median(a, b) == statistics.median(a + b), f"a={a}, b={b}"


def test_logarithmic_reads():
    rng = random.Random(44)
    a_vals = sorted(rng.randint(-10**9, 10**9) for _ in range(200_000))
    b_vals = sorted(rng.randint(-10**9, 10**9) for _ in range(300_001))
    a, b = ProbeArray(a_vals), ProbeArray(b_vals)
    assert task.find_median_sorted_arrays(a, b) == statistics.median(a_vals + b_vals)
    reads = a.reads + b.reads
    limit = 8 * (math.floor(math.log2(len(a_vals) + len(b_vals))) + 2)
    assert reads <= limit, f"Read {reads} elements (limit {limit}); merging is O(m + n)"
