import random

import pytest

from common.loader import load_task

task = load_task(__file__)
CQ = task.CircularQueue


def test_example():
    q = CQ(3)
    assert [q.enqueue(1), q.enqueue(2), q.enqueue(3)] == [True, True, True]
    assert q.enqueue(4) is False
    assert q.rear() == 3
    assert q.is_full()
    assert q.dequeue() == 1
    assert q.enqueue(4) is True
    assert q.rear() == 4
    assert q.front() == 2


@pytest.mark.parametrize("k", [0, -1])
def test_invalid_capacity(k):
    with pytest.raises(ValueError):
        CQ(k)


def test_new_queue():
    q = CQ(2)
    assert q.is_empty() and not q.is_full()
    assert len(q) == 0


@pytest.mark.parametrize("method", ["dequeue", "front", "rear"])
def test_empty_raises(method):
    with pytest.raises(IndexError):
        getattr(CQ(3), method)()


def test_capacity_one():
    q = CQ(1)
    assert q.enqueue("a") is True
    assert q.is_full() and not q.is_empty()
    assert q.front() == "a" == q.rear()
    assert q.enqueue("b") is False
    assert q.dequeue() == "a"
    assert q.is_empty() and not q.is_full()
    assert q.enqueue("c") is True
    assert q.front() == "c"


def test_full_enqueue_does_not_change_state():
    q = CQ(2)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert len(q) == 2
    assert q.front() == 1 and q.rear() == 2


def test_wraps_around_many_times():
    q = CQ(3)
    q.enqueue(0)
    q.enqueue(1)
    for i in range(2, 50):
        assert q.enqueue(i) is True
        assert q.dequeue() == i - 2
        assert q.front() == i - 1
        assert q.rear() == i
        assert len(q) == 2


def test_fill_drain_fill():
    q = CQ(4)
    for round_ in range(3):
        for i in range(4):
            assert q.enqueue(round_ * 10 + i)
        assert q.is_full()
        assert [q.dequeue() for _ in range(4)] == [round_ * 10 + i for i in range(4)]
        assert q.is_empty()


def test_rear_after_wrap_to_index_zero():
    q = CQ(3)
    for v in [1, 2, 3]:
        q.enqueue(v)
    q.dequeue()
    q.enqueue(4)  # lands in physical slot 0
    assert q.rear() == 4
    assert q.front() == 2


def test_none_values():
    q = CQ(2)
    q.enqueue(None)
    assert not q.is_empty()
    assert len(q) == 1
    assert q.dequeue() is None


def test_does_not_grow_or_use_deque():
    q = CQ(2)
    assert q.enqueue(1)
    assert "deque" not in vars(task), "use a fixed-size list, not collections.deque"


def test_randomized_against_model():
    rng = random.Random(622)
    for k in range(1, 8):
        q, model = CQ(k), []
        for _ in range(500):
            if rng.random() < 0.5:
                v = rng.randint(0, 99)
                ok = q.enqueue(v)
                assert ok is (len(model) < k)
                if ok:
                    model.append(v)
            elif model:
                assert q.dequeue() == model.pop(0)
            assert len(q) == len(model)
            assert q.is_empty() == (not model)
            assert q.is_full() == (len(model) == k)
            if model:
                assert q.front() == model[0]
                assert q.rear() == model[-1]


def test_operations_are_constant_time():
    q = CQ(200_000)
    for i in range(200_000):
        q.enqueue(i)
    for i in range(200_000):
        assert q.dequeue() == i
