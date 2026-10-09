import random

import pytest

from common.loader import load_task

task = load_task(__file__)
Stack = task.Stack


def test_new_stack_is_empty():
    s = Stack()
    assert s.is_empty()
    assert len(s) == 0
    assert s.to_list() == []


def test_pop_empty_raises():
    with pytest.raises(IndexError):
        Stack().pop()


def test_peek_empty_raises():
    with pytest.raises(IndexError):
        Stack().peek()


def test_lifo_order():
    s = Stack()
    for v in [1, 2, 3]:
        s.push(v)
    assert [s.pop(), s.pop(), s.pop()] == [3, 2, 1]
    assert s.is_empty()


def test_peek_does_not_remove():
    s = Stack()
    s.push("a")
    s.push("b")
    assert s.peek() == "b"
    assert s.peek() == "b"
    assert len(s) == 2


def test_len_tracks_pushes_and_pops():
    s = Stack()
    for i in range(5):
        s.push(i)
        assert len(s) == i + 1
    s.pop()
    assert len(s) == 4


def test_to_list_bottom_to_top():
    s = Stack()
    for v in [1, 2, 3]:
        s.push(v)
    assert s.to_list() == [1, 2, 3]


def test_to_list_returns_a_copy():
    s = Stack()
    s.push(1)
    snapshot = s.to_list()
    snapshot.append(99)
    assert s.to_list() == [1], "to_list() must return a copy, not the internal list"
    assert len(s) == 1


def test_push_after_emptying():
    s = Stack()
    s.push(1)
    s.pop()
    with pytest.raises(IndexError):
        s.pop()
    s.push(2)
    assert s.peek() == 2


def test_none_and_falsy_values():
    s = Stack()
    s.push(None)
    s.push(0)
    assert not s.is_empty()
    assert s.pop() == 0
    assert s.pop() is None
    assert s.is_empty()


def test_separate_instances_do_not_share_state():
    a, b = Stack(), Stack()
    a.push(1)
    assert b.is_empty(), "don't use a mutable class attribute / default argument for storage"


def test_randomized_against_list():
    rng = random.Random(3)
    s, model = Stack(), []
    for _ in range(2000):
        if model and rng.random() < 0.45:
            assert s.pop() == model.pop()
        else:
            v = rng.randint(-100, 100)
            s.push(v)
            model.append(v)
        assert len(s) == len(model)
        if model:
            assert s.peek() == model[-1]


def test_operations_are_constant_time():
    s = Stack()
    for i in range(300_000):
        s.push(i)
    for i in range(300_000):
        assert s.pop() == 299_999 - i
