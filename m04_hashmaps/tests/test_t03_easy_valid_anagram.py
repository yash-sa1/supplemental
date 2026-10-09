import random

import pytest

from common.loader import load_task

task = load_task(__file__)


def test_example_1():
    assert task.is_anagram("anagram", "nagaram") is True


def test_example_2():
    assert task.is_anagram("rat", "car") is False


def test_both_empty():
    assert task.is_anagram("", "") is True


def test_one_empty():
    assert task.is_anagram("a", "") is False
    assert task.is_anagram("", "a") is False


def test_same_letters_different_counts():
    assert task.is_anagram("aab", "abb") is False


def test_different_lengths_same_letter_set():
    assert task.is_anagram("abc", "abcc") is False
    assert task.is_anagram("abcc", "abc") is False


def test_identical_strings():
    assert task.is_anagram("listen", "listen") is True


def test_case_sensitive():
    assert task.is_anagram("Abc", "abc") is False


def test_unicode_and_spaces():
    assert task.is_anagram("héllo wörld", "wörld héllo") is True
    assert task.is_anagram("🙂🙃", "🙃🙂") is True


@pytest.mark.parametrize("s, t", [("a", "a"), ("ab", "ba"), ("abc", "cab")])
def test_small_true_cases(s, t):
    assert task.is_anagram(s, t) is True


def test_does_not_use_counter():
    assert task.is_anagram("ab", "ba") is True
    assert "Counter" not in vars(task), "build the counts with a plain dict"


def test_randomized():
    rng = random.Random(242)
    for _ in range(500):
        s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        t = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        assert task.is_anagram(s, t) is (sorted(s) == sorted(t)), f"s={s!r}, t={t!r}"


def test_long_strings():
    rng = random.Random(2420)
    s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(100_000))
    t = "".join(rng.sample(s, len(s)))
    assert task.is_anagram(s, t) is True
    assert task.is_anagram(s, t[:-1] + ("a" if t[-1] != "a" else "b")) is False
