import random

import pytest

from common.loader import load_task

task = load_task(__file__)
HashMap = task.HashMap


class Collide:
    """Every instance hashes to the same bucket: forces chaining."""

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return 42

    def __eq__(self, other):
        return isinstance(other, Collide) and self.name == other.name

    def __repr__(self):
        return f"Collide({self.name!r})"


def expected_capacity(n):
    cap = 8
    while n > 0.75 * cap:
        cap *= 2
    return cap


# --- basics -------------------------------------------------------------------

def test_new_map_is_empty():
    m = HashMap()
    assert len(m) == 0
    assert m.capacity == 8
    assert m.keys() == [] and m.values() == [] and m.items() == []


def test_set_and_get():
    m = HashMap()
    m["apple"] = 3
    m["pear"] = 7
    assert m["apple"] == 3
    assert m["pear"] == 7
    assert len(m) == 2


def test_overwrite_does_not_grow():
    m = HashMap()
    m["apple"] = 3
    m["apple"] = 5
    assert m["apple"] == 5
    assert len(m) == 1


def test_missing_key_raises_keyerror():
    m = HashMap()
    m["a"] = 1
    with pytest.raises(KeyError):
        m["b"]


def test_contains():
    m = HashMap()
    m["a"] = 1
    assert "a" in m
    assert "b" not in m


def test_get_with_default():
    m = HashMap()
    m["a"] = 1
    assert m.get("a") == 1
    assert m.get("b") is None
    assert m.get("b", 0) == 0


def test_stored_none_value_is_not_missing():
    m = HashMap()
    m["k"] = None
    assert "k" in m
    assert m["k"] is None
    assert m.get("k", "default") is None


def test_delete():
    m = HashMap()
    m["a"] = 1
    m["b"] = 2
    del m["a"]
    assert "a" not in m
    assert len(m) == 1
    with pytest.raises(KeyError):
        m["a"]


def test_delete_missing_raises_keyerror():
    m = HashMap()
    with pytest.raises(KeyError):
        del m["nope"]


def test_delete_then_reinsert():
    m = HashMap()
    m["a"] = 1
    del m["a"]
    m["a"] = 2
    assert m["a"] == 2 and len(m) == 1


def test_keys_values_items_iter():
    m = HashMap()
    data = {"x": 1, "y": 2, "z": 3}
    for k, v in data.items():
        m[k] = v
    assert sorted(m.keys()) == ["x", "y", "z"]
    assert sorted(m.values()) == [1, 2, 3]
    assert sorted(m.items()) == [("x", 1), ("y", 2), ("z", 3)]
    assert sorted(m) == ["x", "y", "z"]


# --- key types ----------------------------------------------------------------

def test_various_hashable_keys():
    m = HashMap()
    keys = [0, -1, -12345, 3.5, "", "text", (1, 2), None, True, frozenset({1})]
    for i, k in enumerate(keys):
        m[k] = i
    for i, k in enumerate(keys):
        assert m[k] == i, f"key {k!r}"


def test_equal_keys_are_the_same_key():
    # 1 == 1.0 and hash(1) == hash(1.0), so they're one key (same as dict)
    m = HashMap()
    m[1] = "int"
    m[1.0] = "float"
    assert len(m) == 1
    assert m[1] == "float"


def test_unhashable_key_raises_typeerror():
    m = HashMap()
    with pytest.raises(TypeError):
        m[[1, 2]] = "list keys aren't hashable"


# --- collisions ---------------------------------------------------------------

def test_colliding_keys_are_all_stored():
    m = HashMap()
    for name in "abcde":
        m[Collide(name)] = name.upper()
    assert len(m) == 5
    for name in "abcde":
        assert m[Collide(name)] == name.upper()


def test_delete_from_middle_of_chain():
    m = HashMap()
    for name in "abcde":
        m[Collide(name)] = name
    del m[Collide("c")]
    assert Collide("c") not in m
    for name in "abde":
        assert m[Collide(name)] == name
    assert len(m) == 4


def test_overwrite_inside_chain():
    m = HashMap()
    for name in "abc":
        m[Collide(name)] = 0
    m[Collide("b")] = 99
    assert m[Collide("b")] == 99
    assert len(m) == 3


def test_missing_key_in_nonempty_bucket():
    m = HashMap()
    m[Collide("a")] = 1
    assert Collide("z") not in m
    with pytest.raises(KeyError):
        m[Collide("z")]


# --- resizing -----------------------------------------------------------------

def test_resize_threshold():
    m = HashMap()
    for i in range(6):
        m[i] = i
    assert m.capacity == 8, "6 keys / 8 buckets = 0.75: not over the limit yet"
    m[6] = 6
    assert m.capacity == 16, "7 keys / 8 buckets > 0.75: should have doubled"


def test_overwrite_does_not_trigger_resize():
    m = HashMap()
    for i in range(6):
        m[i] = i
    for _ in range(10):
        m[0] = "again"
    assert m.capacity == 8


@pytest.mark.parametrize("n", [1, 7, 13, 25, 100, 1000])
def test_capacity_grows_by_doubling(n):
    m = HashMap()
    for i in range(n):
        m[f"key{i}"] = i
    assert m.capacity == expected_capacity(n)


def test_all_entries_survive_resizes():
    m = HashMap()
    for i in range(1000):
        m[i * 7919] = i
    assert len(m) == 1000
    for i in range(1000):
        assert m[i * 7919] == i


def test_no_builtin_dict_or_set_inside():
    m = HashMap()
    for i in range(20):
        m[i] = i

    def walk(obj, depth=0):
        assert not isinstance(obj, (dict, set, frozenset)), "don't use dict/set inside your HashMap"
        if depth < 3 and isinstance(obj, (list, tuple)):
            for item in obj:
                walk(item, depth + 1)

    for value in vars(m).values():
        walk(value)


def test_separate_instances_do_not_share_state():
    a, b = HashMap(), HashMap()
    a["x"] = 1
    assert "x" not in b
    assert len(b) == 0


# --- stress -------------------------------------------------------------------

def test_randomized_against_dict():
    rng = random.Random(4)
    m, model = HashMap(), {}
    for _ in range(5000):
        k = rng.randint(0, 200)
        op = rng.random()
        if op < 0.5:
            m[k] = model[k] = rng.randint(0, 999)
        elif op < 0.75:
            if k in model:
                del model[k]
                del m[k]
            else:
                with pytest.raises(KeyError):
                    del m[k]
        else:
            assert (k in m) == (k in model)
            assert m.get(k) == model.get(k)
        assert len(m) == len(model)
    assert sorted(m.items()) == sorted(model.items())


def test_large_is_fast():
    # without resizing, chains grow to thousands of entries and this times out
    m = HashMap()
    n = 100_000
    for i in range(n):
        m[f"k{i}"] = i
    for i in range(n):
        assert m[f"k{i}"] == i
    assert len(m) == n
