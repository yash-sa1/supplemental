import random

import pytest

from common.loader import load_task
from m02_linked_lists.framework import ListNode, to_list

task = load_task(__file__)
SLL = task.SinglyLinkedList


def make(values):
    sll = SLL()
    for v in values:
        sll.append(v)
    return sll


def check(sll, expected):
    """The list must agree with `expected` through every view of it."""
    assert to_list(sll.head) == expected, "walking .head -> .next chain gives the wrong values"
    assert len(sll) == len(expected), "len() is out of sync with the nodes"
    assert list(sll) == expected, "__iter__ gives the wrong values"
    assert sll.to_list() == expected
    assert sll.is_empty() == (not expected)


# --- empty list -------------------------------------------------------------

def test_new_list_is_empty():
    sll = SLL()
    assert sll.head is None
    check(sll, [])


def test_pop_front_empty_raises():
    with pytest.raises(IndexError):
        SLL().pop_front()


def test_get_empty_raises():
    with pytest.raises(IndexError):
        SLL().get(0)


def test_remove_at_empty_raises():
    with pytest.raises(IndexError):
        SLL().remove_at(0)


def test_remove_and_find_on_empty():
    sll = SLL()
    assert sll.remove(1) is False
    assert sll.find(1) == -1
    assert 1 not in sll


# --- adding -------------------------------------------------------------------

def test_append():
    check(make([1, 2, 3]), [1, 2, 3])


def test_prepend():
    sll = SLL()
    for v in [3, 2, 1]:
        sll.prepend(v)
    check(sll, [1, 2, 3])


def test_head_is_a_listnode():
    sll = make([5])
    assert isinstance(sll.head, ListNode)
    assert sll.head.val == 5 and sll.head.next is None


def test_prepend_then_append_on_empty():
    # prepending into an empty list must also set up the tail for append
    sll = SLL()
    sll.prepend(1)
    sll.append(2)
    check(sll, [1, 2])


def test_insert_front_middle_end():
    sll = make([1, 3])
    sll.insert(0, 0)
    sll.insert(2, 2)
    sll.insert(4, 4)
    check(sll, [0, 1, 2, 3, 4])


def test_insert_into_empty():
    sll = SLL()
    sll.insert(0, "x")
    check(sll, ["x"])


def test_insert_at_end_then_append():
    sll = make([1])
    sll.insert(1, 2)  # at the end: tail must be updated
    sll.append(3)
    check(sll, [1, 2, 3])


@pytest.mark.parametrize("index", [-1, 4, 100])
def test_insert_out_of_range_raises(index):
    sll = make([1, 2, 3])
    with pytest.raises(IndexError):
        sll.insert(index, 9)
    check(sll, [1, 2, 3])


# --- reading ------------------------------------------------------------------

def test_get():
    sll = make(["a", "b", "c"])
    assert [sll.get(i) for i in range(3)] == ["a", "b", "c"]


@pytest.mark.parametrize("index", [-1, 3, 50])
def test_get_out_of_range_raises(index):
    with pytest.raises(IndexError):
        make([1, 2, 3]).get(index)


def test_find_and_contains():
    sll = make([4, 5, 4, 6])
    assert sll.find(4) == 0
    assert sll.find(6) == 3
    assert sll.find(7) == -1
    assert 5 in sll
    assert 7 not in sll


def test_contains_falsy_values():
    sll = make([0, None, ""])
    assert 0 in sll and None in sll and "" in sll
    assert sll.find(None) == 1


# --- removing -----------------------------------------------------------------

def test_pop_front():
    sll = make([1, 2, 3])
    assert sll.pop_front() == 1
    check(sll, [2, 3])


def test_pop_front_until_empty_then_reuse():
    sll = make([1, 2])
    sll.pop_front()
    sll.pop_front()
    check(sll, [])
    sll.append(9)  # tail must have been reset
    check(sll, [9])


def test_remove_at_front_middle_end():
    sll = make([0, 1, 2, 3, 4])
    assert sll.remove_at(0) == 0
    assert sll.remove_at(1) == 2
    assert sll.remove_at(2) == 4
    check(sll, [1, 3])


def test_remove_at_last_then_append():
    # Classic bug: forgetting to move the tail back after removing the last node
    sll = make([1, 2, 3])
    assert sll.remove_at(2) == 3
    sll.append(4)
    check(sll, [1, 2, 4])


@pytest.mark.parametrize("index", [-1, 3])
def test_remove_at_out_of_range_raises(index):
    sll = make([1, 2, 3])
    with pytest.raises(IndexError):
        sll.remove_at(index)
    check(sll, [1, 2, 3])


def test_remove_value_first_occurrence_only():
    sll = make([1, 2, 1, 2])
    assert sll.remove(2) is True
    check(sll, [1, 1, 2])


def test_remove_value_head():
    sll = make([1, 2])
    assert sll.remove(1) is True
    check(sll, [2])


def test_remove_value_tail_then_append():
    sll = make([1, 2])
    assert sll.remove(2) is True
    sll.append(3)
    check(sll, [1, 3])


def test_remove_only_element_then_append():
    sll = make([1])
    assert sll.remove(1) is True
    check(sll, [])
    sll.append(2)
    check(sll, [2])


def test_remove_missing_value():
    sll = make([1, 2])
    assert sll.remove(3) is False
    check(sll, [1, 2])


# --- stress -------------------------------------------------------------------

def test_randomized_against_python_list():
    rng = random.Random(2)
    for _ in range(40):
        sll, model = SLL(), []
        for _ in range(60):
            op = rng.choice(["append", "prepend", "insert", "pop_front", "remove_at", "remove", "get"])
            v = rng.randint(0, 5)
            if op == "append":
                sll.append(v); model.append(v)
            elif op == "prepend":
                sll.prepend(v); model.insert(0, v)
            elif op == "insert":
                i = rng.randint(0, len(model))
                sll.insert(i, v); model.insert(i, v)
            elif op == "pop_front" and model:
                assert sll.pop_front() == model.pop(0)
            elif op == "remove_at" and model:
                i = rng.randrange(len(model))
                assert sll.remove_at(i) == model.pop(i)
            elif op == "remove":
                expected = v in model
                if expected:
                    model.remove(v)
                assert sll.remove(v) is expected
            elif op == "get" and model:
                i = rng.randrange(len(model))
                assert sll.get(i) == model[i]
            check(sll, model)


def test_append_is_constant_time():
    sll = SLL()
    for i in range(200_000):  # O(n) append would be ~2*10^10 steps: timeout
        sll.append(i)
    assert len(sll) == 200_000
    assert sll.get(199_999) == 199_999


def test_len_is_constant_time():
    sll = make(range(100_000))
    for _ in range(100_000):  # walking the list inside __len__ would time out
        assert len(sll) == 100_000
