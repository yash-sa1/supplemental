import random

import pytest

from common.loader import load_task

task = load_task(__file__)
MinStack = task.MinStack


def test_example():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    assert s.pop() == -3
    assert s.top() == 0
    assert s.get_min() == -2


@pytest.mark.parametrize("method", ["pop", "top", "get_min"])
def test_empty_raises(method):
    with pytest.raises(IndexError):
        getattr(MinStack(), method)()


def test_single_element():
    s = MinStack()
    s.push(5)
    assert s.top() == 5 == s.get_min()
    assert len(s) == 1


def test_min_restored_after_pop():
    s = MinStack()
    for v in [5, 3, 7, 1]:
        s.push(v)
    assert s.get_min() == 1
    s.pop()
    assert s.get_min() == 3
    s.pop()
    assert s.get_min() == 3
    s.pop()
    assert s.get_min() == 5


def test_duplicate_minimums():
    # Classic bug with a separate min-stack: only pushing when val < min (not <=)
    s = MinStack()
    s.push(1)
    s.push(1)
    s.push(2)
    s.pop()
    s.pop()
    assert s.get_min() == 1


def test_increasing_pushes():
    s = MinStack()
    for v in range(10):
        s.push(v)
        assert s.get_min() == 0


def test_decreasing_pushes():
    s = MinStack()
    for v in range(10, 0, -1):
        s.push(v)
        assert s.get_min() == v


def test_negatives_and_zero():
    s = MinStack()
    s.push(0)
    s.push(-1)
    s.push(-1)
    s.pop()
    assert s.get_min() == -1
    s.pop()
    assert s.get_min() == 0


def test_empty_then_reuse():
    s = MinStack()
    s.push(1)
    s.pop()
    with pytest.raises(IndexError):
        s.get_min()
    s.push(10)
    assert s.get_min() == 10


def test_randomized_against_model():
    rng = random.Random(155)
    s, model = MinStack(), []
    for _ in range(3000):
        if model and rng.random() < 0.4:
            assert s.pop() == model.pop()
        else:
            v = rng.randint(-5, 5)
            s.push(v)
            model.append(v)
        assert len(s) == len(model)
        if model:
            assert s.top() == model[-1]
            assert s.get_min() == min(model)


def test_get_min_is_constant_time():
    s = MinStack()
    n = 100_000
    for i in range(n, 0, -1):
        s.push(i)
    s.push(0)
    s.pop()
    for _ in range(n):  # an O(n) scan per call would be 10^10 steps
        assert s.get_min() == 1
