import random

import pytest

from common.loader import load_task

task = load_task(__file__)


@pytest.mark.parametrize("s", ["()[]{}", "([{}])", "()", "{[]}", "(((())))", "[](){}[{()}]"])
def test_valid(s):
    assert task.is_valid(s) is True


@pytest.mark.parametrize("s", ["(]", "([)]", "{[}]", "((", "))", "(()", "())", "][", "}{"])
def test_invalid(s):
    assert task.is_valid(s) is False


def test_empty_string_is_valid():
    assert task.is_valid("") is True


def test_single_opener():
    assert task.is_valid("(") is False


def test_single_closer_on_empty_stack():
    # popping from an empty stack must not crash
    assert task.is_valid(")") is False
    assert task.is_valid("]") is False


def test_closer_after_balanced_prefix():
    assert task.is_valid("()]") is False


def test_counting_is_not_enough():
    # right counts of each type, wrong order: a counter-based solution passes this incorrectly
    assert task.is_valid("([)]") is False
    assert task.is_valid(")(") is False


def test_unclosed_at_end():
    assert task.is_valid("{[]") is False


def gen_valid(rng, depth=0):
    parts = []
    for _ in range(rng.randint(0, 3 if depth < 4 else 0)):
        o, c = rng.choice(["()", "[]", "{}"])
        parts.append(o + gen_valid(rng, depth + 1) + c)
    return "".join(parts)


def test_randomized_valid_strings():
    rng = random.Random(20)
    for _ in range(300):
        s = gen_valid(rng)
        assert task.is_valid(s) is True, s


def test_randomized_single_corruption_makes_invalid():
    rng = random.Random(21)
    for _ in range(300):
        s = gen_valid(rng)
        if not s:
            continue
        i = rng.randrange(len(s))
        # drop one character: bracket count becomes odd -> must be invalid
        assert task.is_valid(s[:i] + s[i + 1 :]) is False, s[:i] + s[i + 1 :]


def test_long_valid():
    assert task.is_valid("([{" * 30_000 + "}])" * 30_000) is True


def test_long_invalid_at_the_very_end():
    assert task.is_valid("(" * 50_000 + ")" * 49_999 + "]") is False
