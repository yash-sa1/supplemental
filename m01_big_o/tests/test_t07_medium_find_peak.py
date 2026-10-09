import math
import random

from common.loader import load_task
from common.probes import ProbeArray

task = load_task(__file__)


def is_peak(values, i):
    if not isinstance(i, int) or not 0 <= i < len(values):
        return False
    left = values[i - 1] if i > 0 else -math.inf
    right = values[i + 1] if i + 1 < len(values) else -math.inf
    return left < values[i] > right


def check(values):
    i = task.find_peak(ProbeArray(values))
    assert is_peak(values, i), f"arr={values}: index {i} is not a peak"
    return i


def test_example_1():
    assert check([1, 2, 3, 1]) == 2


def test_example_2_either_peak():
    assert check([1, 2, 1, 3, 5, 6, 4]) in (1, 5)


def test_single_element():
    assert check([7]) == 0


def test_two_elements():
    assert check([1, 2]) == 1
    assert check([2, 1]) == 0


def test_strictly_increasing_peak_is_last():
    assert check([1, 2, 3, 4, 5]) == 4


def test_strictly_decreasing_peak_is_first():
    assert check([5, 4, 3, 2, 1]) == 0


def test_valley_shape():
    assert check([3, 1, 3]) in (0, 2)


def test_zigzag():
    check([1, 3, 2, 4, 3, 5, 4])


def test_negative_values():
    check([-5, -3, -4, -10])


def test_randomized():
    rng = random.Random(162)
    for _ in range(500):
        n = rng.randint(1, 30)
        values = [rng.randint(-20, 20)]
        while len(values) < n:
            v = rng.randint(-20, 20)
            if v != values[-1]:
                values.append(v)
        check(values)


def test_logarithmic_on_long_climb():
    n = 1_000_000
    arr = ProbeArray(range(n))  # only peak is the very last element
    assert task.find_peak(arr) == n - 1
    limit = 4 * (math.floor(math.log2(n)) + 2)
    assert arr.reads <= limit, f"Read {arr.reads} elements (limit {limit}); scanning is O(n)"


def test_logarithmic_on_mountain():
    n = 1_000_001
    peak = 700_000
    values = list(range(peak + 1)) + list(range(peak - 1, peak - (n - peak), -1))
    arr = ProbeArray(values)
    assert task.find_peak(arr) == peak
    assert arr.reads <= 4 * (math.floor(math.log2(n)) + 2)
