import random

import pytest

from common.loader import load_task

task = load_task(__file__)
MyQueue = task.MyQueue


def test_example():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert q.empty() is False


def test_new_queue_empty():
    assert MyQueue().empty() is True


def test_pop_empty_raises():
    with pytest.raises(IndexError):
        MyQueue().pop()


def test_peek_empty_raises():
    with pytest.raises(IndexError):
        MyQueue().peek()


def test_fifo_order():
    q = MyQueue()
    for v in range(5):
        q.push(v)
    assert [q.pop() for _ in range(5)] == [0, 1, 2, 3, 4]
    assert q.empty()


def test_push_after_partial_pop_keeps_order():
    # The key bug: pushing new items while the output stack still has old ones
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    q.push(3)
    q.push(4)
    assert q.peek() == 2
    assert [q.pop(), q.pop(), q.pop()] == [2, 3, 4]
    assert q.empty()


def test_empty_after_everything_popped_then_reuse():
    q = MyQueue()
    q.push("a")
    q.pop()
    assert q.empty()
    q.push("b")
    assert q.peek() == "b"


def test_falsy_values():
    q = MyQueue()
    q.push(0)
    q.push(None)
    assert q.empty() is False
    assert q.pop() == 0
    assert q.pop() is None


def test_randomized_against_model():
    rng = random.Random(232)
    q, model = MyQueue(), []
    for _ in range(3000):
        r = rng.random()
        if model and r < 0.35:
            assert q.pop() == model.pop(0)
        elif model and r < 0.5:
            assert q.peek() == model[0]
        else:
            v = rng.randint(0, 99)
            q.push(v)
            model.append(v)
        assert q.empty() == (not model)


def test_amortised_constant_time():
    q = MyQueue()
    n = 100_000
    for i in range(n):
        q.push(i)
    # alternating peek/pop/push: moving everything back and forth each call would be O(n^2)
    for i in range(n):
        assert q.peek() == i
        assert q.pop() == i
        q.push(n + i)
    for i in range(n):
        assert q.pop() == n + i
