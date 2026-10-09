import random

from common.loader import load_task

task = load_task(__file__)


def brute(temps):
    out = []
    for i, t in enumerate(temps):
        wait = 0
        for j in range(i + 1, len(temps)):
            if temps[j] > t:
                wait = j - i
                break
        out.append(wait)
    return out


def test_example_1():
    assert task.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_example_2():
    assert task.daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]


def test_example_3():
    assert task.daily_temperatures([30, 60, 90]) == [1, 1, 0]


def test_empty():
    assert task.daily_temperatures([]) == []


def test_single_day():
    assert task.daily_temperatures([50]) == [0]


def test_strictly_decreasing_all_zero():
    assert task.daily_temperatures([90, 80, 70, 60]) == [0, 0, 0, 0]


def test_equal_temperatures_are_not_warmer():
    assert task.daily_temperatures([50, 50, 50]) == [0, 0, 0]
    assert task.daily_temperatures([50, 50, 51]) == [2, 1, 0]


def test_valley_then_peak():
    assert task.daily_temperatures([70, 60, 50, 40, 80]) == [4, 3, 2, 1, 0]


def test_does_not_mutate_input():
    temps = [73, 74, 75, 71]
    task.daily_temperatures(temps)
    assert temps == [73, 74, 75, 71]


def test_randomized_against_brute_force():
    rng = random.Random(739)
    for _ in range(300):
        temps = [rng.randint(30, 40) for _ in range(rng.randint(0, 30))]
        assert task.daily_temperatures(temps) == brute(temps), f"temps={temps}"


def test_large_decreasing_then_spike():
    n = 100_000  # O(n^2) is 5*10^9 steps here
    temps = [30 + (i * 70) // n for i in range(n)][::-1] + [101]
    result = task.daily_temperatures(temps)
    assert result[0] == n
    assert result[-1] == 0


def test_large_random():
    rng = random.Random(7390)
    temps = [rng.randint(30, 100) for _ in range(100_000)]
    result = task.daily_temperatures(temps)
    assert len(result) == len(temps)
    for i in rng.sample(range(len(temps)), 200):
        w = result[i]
        if w:
            assert temps[i + w] > temps[i] and all(t <= temps[i] for t in temps[i + 1 : i + w])
