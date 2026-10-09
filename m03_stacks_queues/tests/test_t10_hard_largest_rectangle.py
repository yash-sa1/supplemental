import random

from common.loader import load_task

task = load_task(__file__)


def brute(heights):
    best = 0
    for i in range(len(heights)):
        low = heights[i]
        for j in range(i, len(heights)):
            low = min(low, heights[j])
            best = max(best, low * (j - i + 1))
    return best


def test_example_1():
    assert task.largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10


def test_example_2():
    assert task.largest_rectangle_area([2, 4]) == 4


def test_empty():
    assert task.largest_rectangle_area([]) == 0


def test_single_bar():
    assert task.largest_rectangle_area([7]) == 7


def test_zero_height_bars():
    assert task.largest_rectangle_area([0, 0, 0]) == 0
    assert task.largest_rectangle_area([0, 3, 0]) == 3


def test_all_equal():
    assert task.largest_rectangle_area([3, 3, 3, 3]) == 12


def test_increasing():
    assert task.largest_rectangle_area([1, 2, 3, 4, 5]) == 9  # 3*3


def test_decreasing():
    assert task.largest_rectangle_area([5, 4, 3, 2, 1]) == 9


def test_wide_short_beats_tall_narrow():
    assert task.largest_rectangle_area([1, 1, 1, 1, 1, 1, 4]) == 7


def test_valley():
    assert task.largest_rectangle_area([4, 2, 0, 3, 2, 5]) == 6


def test_does_not_mutate_input():
    heights = [2, 1, 5, 6, 2, 3]
    task.largest_rectangle_area(heights)
    assert heights == [2, 1, 5, 6, 2, 3]


def test_randomized_against_brute_force():
    rng = random.Random(84)
    for _ in range(400):
        heights = [rng.randint(0, 6) for _ in range(rng.randint(0, 15))]
        assert task.largest_rectangle_area(heights) == brute(heights), f"heights={heights}"


def test_large_increasing():
    n = 100_000
    heights = list(range(1, n + 1))
    # best: height h, width n - h + 1 -> maximised near h = n/2
    expected = max(h * (n - h + 1) for h in range(1, n + 1))
    assert task.largest_rectangle_area(heights) == expected


def test_large_all_equal():
    assert task.largest_rectangle_area([10_000] * 100_000) == 10**9
