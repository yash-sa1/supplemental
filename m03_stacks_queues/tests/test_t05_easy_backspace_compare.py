import random

import pytest

from common.loader import load_task

task = load_task(__file__)


def typed(text):
    out = []
    for ch in text:
        if ch == "#":
            if out:
                out.pop()
        else:
            out.append(ch)
    return "".join(out)


def test_example_1():
    assert task.backspace_compare("ab#c", "ad#c") is True


def test_example_2_both_empty_after():
    assert task.backspace_compare("ab##", "c#d#") is True


def test_example_3_different():
    assert task.backspace_compare("a#c", "b") is False


def test_both_empty():
    assert task.backspace_compare("", "") is True


def test_backspace_on_empty_editor():
    assert task.backspace_compare("###a", "a") is True
    assert task.backspace_compare("a###", "") is True


def test_only_backspaces():
    assert task.backspace_compare("####", "#") is True


def test_no_backspaces():
    assert task.backspace_compare("abc", "abc") is True
    assert task.backspace_compare("abc", "abd") is False


def test_different_lengths_after_typing():
    assert task.backspace_compare("ab", "a") is False
    assert task.backspace_compare("a", "ab") is False


def test_backspace_then_retype():
    assert task.backspace_compare("xy#z", "xz") is True
    assert task.backspace_compare("bxj##tw", "bxo#j##tw") is True


@pytest.mark.parametrize("s, t", [("a##c", "#a#c"), ("bbbextm", "bbb#extm"), ("y#fo##f", "y#f#o##f")])
def test_leetcode_tricky_cases(s, t):
    assert task.backspace_compare(s, t) is (typed(s) == typed(t))


def test_randomized():
    rng = random.Random(844)
    for _ in range(1000):
        s = "".join(rng.choice("ab#") for _ in range(rng.randint(0, 10)))
        t = "".join(rng.choice("ab#") for _ in range(rng.randint(0, 10)))
        assert task.backspace_compare(s, t) is (typed(s) == typed(t)), f"s={s!r}, t={t!r}"


def test_long_strings():
    s = "a" * 100_000 + "#" * 99_999
    assert task.backspace_compare(s, "a") is True
