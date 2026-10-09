import random
from collections import OrderedDict

import pytest

from common.loader import load_task

task = load_task(__file__)
LRU = task.LRUCache


class ModelLRU:
    """Reference behaviour built on OrderedDict (fine in a test, not in your solution)."""

    def __init__(self, capacity):
        self.capacity, self.data = capacity, OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


def test_example():
    c = LRU(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4


@pytest.mark.parametrize("capacity", [0, -1])
def test_invalid_capacity(capacity):
    with pytest.raises(ValueError):
        LRU(capacity)


def test_get_missing():
    assert LRU(2).get("nope") == -1


def test_capacity_one():
    c = LRU(1)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == -1
    assert c.get("b") == 2
    assert len(c) == 1


def test_update_existing_key_does_not_evict():
    c = LRU(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 10)  # update, not insert: nothing evicted
    assert len(c) == 2
    assert c.get(1) == 10
    assert c.get(2) == 2


def test_update_counts_as_use():
    c = LRU(2)
    c.put(1, 1)
    c.put(2, 2)
    c.put(1, 100)  # 1 is now most recent, so 2 is evicted next
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(1) == 100


def test_get_counts_as_use():
    c = LRU(3)
    for k in (1, 2, 3):
        c.put(k, k)
    c.get(1)  # order: 2, 3, 1
    c.put(4, 4)  # evicts 2
    assert c.get(2) == -1
    assert c.get(1) == 1


def test_failed_get_does_not_change_order():
    c = LRU(2)
    c.put(1, 1)
    c.put(2, 2)
    c.get(99)
    c.put(3, 3)  # still evicts 1
    assert c.get(1) == -1


def test_values_can_be_falsy_or_none():
    c = LRU(3)
    c.put("zero", 0)
    c.put("none", None)
    assert c.get("zero") == 0
    assert c.get("none") is None


def test_len():
    c = LRU(3)
    assert len(c) == 0
    for k in range(5):
        c.put(k, k)
    assert len(c) == 3


def test_does_not_use_ordereddict():
    c = LRU(1)
    c.put(1, 1)
    assert "OrderedDict" not in vars(task), "build the recency list yourself with DListNode"


def test_randomized_against_model():
    rng = random.Random(146)
    for capacity in (1, 2, 3, 5, 8):
        c, model = LRU(capacity), ModelLRU(capacity)
        for _ in range(1500):
            k = rng.randint(0, 10)
            if rng.random() < 0.5:
                v = rng.randint(0, 99)
                c.put(k, v)
                model.put(k, v)
            else:
                assert c.get(k) == model.get(k), f"capacity={capacity}, get({k})"
            assert len(c) == len(model.data)


def test_operations_are_constant_time():
    n = 100_000
    c = LRU(n)
    for i in range(n):
        c.put(i, i)
    # touch the oldest key each time: a list-based recency order (list.remove / index) is O(n)
    for i in range(n):
        assert c.get(i) == i
    for i in range(n, 2 * n):
        c.put(i, i)
    assert c.get(0) == -1
    assert c.get(2 * n - 1) == 2 * n - 1
