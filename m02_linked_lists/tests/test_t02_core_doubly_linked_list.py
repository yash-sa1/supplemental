import itertools
import random

import pytest

from common.loader import load_task

task = load_task(__file__)
DLL = task.DoublyLinkedList


def make(values):
    dll = DLL()
    for v in values:
        dll.push_back(v)
    return dll


def check(dll, expected):
    """Forward AND backward traversal must agree: catches broken .prev pointers."""
    forward = list(itertools.islice(iter(dll), len(expected) + 5))
    backward = list(itertools.islice(reversed(dll), len(expected) + 5))
    assert forward == expected, "front-to-back traversal (next pointers) is wrong"
    assert backward == expected[::-1], "back-to-front traversal (prev pointers) is wrong"
    assert len(dll) == len(expected)
    assert dll.to_list() == expected
    assert dll.is_empty() == (not expected)


def test_new_list_is_empty():
    check(DLL(), [])


@pytest.mark.parametrize("method", ["pop_front", "pop_back", "peek_front", "peek_back"])
def test_empty_operations_raise(method):
    with pytest.raises(IndexError):
        getattr(DLL(), method)()


def test_push_back():
    check(make([1, 2, 3]), [1, 2, 3])


def test_push_front():
    dll = DLL()
    for v in [3, 2, 1]:
        dll.push_front(v)
    check(dll, [1, 2, 3])


def test_mixed_pushes():
    dll = DLL()
    dll.push_back(2)
    dll.push_front(1)
    dll.push_back(3)
    check(dll, [1, 2, 3])


def test_peeks_do_not_remove():
    dll = make([1, 2, 3])
    assert dll.peek_front() == 1
    assert dll.peek_back() == 3
    check(dll, [1, 2, 3])


def test_single_element_peeks():
    dll = make([7])
    assert dll.peek_front() == 7 == dll.peek_back()


def test_pop_front_and_back():
    dll = make([1, 2, 3, 4])
    assert dll.pop_front() == 1
    assert dll.pop_back() == 4
    check(dll, [2, 3])


def test_pop_single_element_from_back_then_front_push():
    dll = make([1])
    assert dll.pop_back() == 1
    check(dll, [])
    dll.push_front(2)
    check(dll, [2])


def test_pop_single_element_from_front_then_back_push():
    dll = make([1])
    assert dll.pop_front() == 1
    check(dll, [])
    dll.push_back(2)
    check(dll, [2])


def test_alternate_pops_until_empty():
    dll = make(range(5))
    assert [dll.pop_front(), dll.pop_back(), dll.pop_front(), dll.pop_back(), dll.pop_front()] == [0, 4, 1, 3, 2]
    check(dll, [])
    with pytest.raises(IndexError):
        dll.pop_back()


def test_insert_positions():
    dll = make([1, 3])
    dll.insert(0, 0)
    dll.insert(2, 2)
    dll.insert(4, 4)
    check(dll, [0, 1, 2, 3, 4])


def test_insert_into_empty():
    dll = DLL()
    dll.insert(0, "x")
    check(dll, ["x"])


@pytest.mark.parametrize("index", [-1, 3])
def test_insert_out_of_range(index):
    dll = make([1, 2])
    with pytest.raises(IndexError):
        dll.insert(index, 9)
    check(dll, [1, 2])


def test_remove_at_positions():
    dll = make([0, 1, 2, 3, 4])
    assert dll.remove_at(4) == 4
    assert dll.remove_at(0) == 0
    assert dll.remove_at(1) == 2
    check(dll, [1, 3])


@pytest.mark.parametrize("index", [-1, 2, 10])
def test_remove_at_out_of_range(index):
    dll = make([1, 2])
    with pytest.raises(IndexError):
        dll.remove_at(index)
    check(dll, [1, 2])


def test_get_every_index():
    values = list("abcdefg")
    dll = make(values)
    for i, v in enumerate(values):
        assert dll.get(i) == v


@pytest.mark.parametrize("index", [-1, 3])
def test_get_out_of_range(index):
    with pytest.raises(IndexError):
        make([1, 2, 3]).get(index)


def test_stores_none_and_falsy_values():
    dll = make([None, 0, False])
    assert dll.pop_front() is None
    check(dll, [0, False])


def test_randomized_against_python_list():
    rng = random.Random(22)
    for _ in range(40):
        dll, model = DLL(), []
        for _ in range(60):
            op = rng.choice(["push_front", "push_back", "pop_front", "pop_back", "insert", "remove_at", "get"])
            v = rng.randint(0, 99)
            if op == "push_front":
                dll.push_front(v); model.insert(0, v)
            elif op == "push_back":
                dll.push_back(v); model.append(v)
            elif op == "pop_front" and model:
                assert dll.pop_front() == model.pop(0)
            elif op == "pop_back" and model:
                assert dll.pop_back() == model.pop()
            elif op == "insert":
                i = rng.randint(0, len(model))
                dll.insert(i, v); model.insert(i, v)
            elif op == "remove_at" and model:
                i = rng.randrange(len(model))
                assert dll.remove_at(i) == model.pop(i)
            elif op == "get" and model:
                i = rng.randrange(len(model))
                assert dll.get(i) == model[i]
            check(dll, model)


def test_both_ends_are_constant_time():
    dll = DLL()
    n = 200_000
    for i in range(n):
        dll.push_back(i)
        dll.push_front(-i)
    for _ in range(n):
        dll.pop_back()
        dll.pop_front()
    assert len(dll) == 0
