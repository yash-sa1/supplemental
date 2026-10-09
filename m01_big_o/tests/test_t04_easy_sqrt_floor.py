import inspect
import math

import pytest

from common.loader import load_task

task = load_task(__file__)


def test_example_perfect_square():
    assert task.sqrt_floor(4) == 2


def test_example_rounds_down():
    assert task.sqrt_floor(8) == 2


@pytest.mark.parametrize("x, expected", [(0, 0), (1, 1), (2, 1), (3, 1)])
def test_tiny_values(x, expected):
    assert task.sqrt_floor(x) == expected


@pytest.mark.parametrize("x, expected", [(15, 3), (16, 4), (17, 4), (24, 4), (25, 5), (26, 5)])
def test_around_perfect_squares(x, expected):
    assert task.sqrt_floor(x) == expected


def test_first_2000_values():
    for x in range(2000):
        assert task.sqrt_floor(x) == math.isqrt(x), f"sqrt_floor({x})"


def test_int32_max():
    # mid * mid overflows in Java/C++ here; Python ints are unbounded but still a classic edge case
    assert task.sqrt_floor(2**31 - 1) == 46340


def test_very_large():
    assert task.sqrt_floor(10**18) == 10**9
    assert task.sqrt_floor(10**18 - 1) == 10**9 - 1


def test_returns_int_not_float():
    result = task.sqrt_floor(10)
    assert type(result) is int, f"Expected int, got {type(result).__name__}"


def test_negative_raises():
    with pytest.raises(ValueError):
        task.sqrt_floor(-1)


def test_no_builtin_power_functions():
    assert task.sqrt_floor(16) == 4
    source = inspect.getsource(task.sqrt_floor)
    code_lines = [line.split("#")[0] for line in source.splitlines()]
    code = "\n".join(code_lines)
    for banned in ("**", "pow(", "sqrt(", "isqrt("):
        assert banned not in code, f"Don't use {banned!r}; binary search for the answer instead"
