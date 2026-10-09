import random

import pytest

from common.loader import load_task

task = load_task(__file__)
Queue = task.LinkedQueue


def test_new_queue_is_empty():
    q = Queue()
    assert q.is_empty()
    assert len(q) == 0
    assert q.to_list() == []


def test_dequeue_empty_raises():
    with pytest.raises(IndexError):
        Queue().dequeue()


def test_peek_empty_raises():
    with pytest.raises(IndexError):
        Queue().peek()


def test_fifo_order():
    q = Queue()
    for v in [1, 2, 3]:
        q.enqueue(v)
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == [1, 2, 3]
    assert q.is_empty()


def test_peek_does_not_remove():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert len(q) == 2


def test_to_list_front_to_back():
    q = Queue()
    for v in [1, 2, 3]:
        q.enqueue(v)
    q.dequeue()
    assert q.to_list() == [2, 3]


def test_empty_then_reuse():
    # Classic bug: after dequeuing the last item, tail still points at the old node
    q = Queue()
    q.enqueue(1)
    assert q.dequeue() == 1
    assert q.is_empty()
    q.enqueue(2)
    q.enqueue(3)
    assert q.to_list() == [2, 3]
    assert q.dequeue() == 2


def test_interleaved():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    with pytest.raises(IndexError):
        q.dequeue()


def test_none_and_falsy_values():
    q = Queue()
    q.enqueue(None)
    q.enqueue(0)
    assert len(q) == 2
    assert q.dequeue() is None
    assert q.dequeue() == 0


def test_separate_instances_do_not_share_state():
    a, b = Queue(), Queue()
    a.enqueue(1)
    assert b.is_empty()


def test_does_not_use_deque():
    q = Queue()
    q.enqueue(1)
    assert q.dequeue() == 1
    assert "deque" not in vars(task), "build the queue from nodes instead of collections.deque"


def test_randomized_against_model():
    rng = random.Random(33)
    q, model = Queue(), []
    for _ in range(2000):
        if model and rng.random() < 0.45:
            assert q.dequeue() == model.pop(0)
        else:
            v = rng.randint(0, 1000)
            q.enqueue(v)
            model.append(v)
        assert len(q) == len(model)
        if model:
            assert q.peek() == model[0]
    assert q.to_list() == model


def test_dequeue_is_constant_time():
    q = Queue()
    n = 1_000_000  # list.pop(0) is O(n) per call: ~1 minute here -> timeout
    for i in range(n):
        q.enqueue(i)
    for i in range(n):
        assert q.dequeue() == i
