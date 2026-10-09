import pytest

from common.loader import load_task

task = load_task(__file__)


def rpn(expr):
    return task.eval_rpn(expr.split())


def test_example_1():
    assert task.eval_rpn(["2", "1", "+", "3", "*"]) == 9


def test_example_2():
    assert task.eval_rpn(["4", "13", "5", "/", "+"]) == 6


def test_example_3():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert task.eval_rpn(tokens) == 22


def test_single_number():
    assert rpn("42") == 42
    assert rpn("-7") == -7


def test_operand_order_subtraction():
    assert rpn("10 3 -") == 7, "first popped value is the RIGHT operand"


def test_operand_order_division():
    assert rpn("12 4 /") == 3


@pytest.mark.parametrize("expr, expected", [
    ("7 2 /", 3),
    ("-7 2 /", -3),
    ("7 -2 /", -3),
    ("-7 -2 /", 3),
    ("1 3 /", 0),
    ("-1 3 /", 0),
    ("6 3 /", 2),
    ("-6 3 /", -2),
])
def test_division_truncates_toward_zero(expr, expected):
    assert rpn(expr) == expected


def test_returns_int():
    assert type(rpn("7 2 /")) is int


def test_negative_numbers_are_operands_not_operators():
    assert rpn("-3 -4 *") == 12
    assert rpn("5 -3 -") == 8


def test_zero_operands():
    assert rpn("0 5 *") == 0
    assert rpn("0 5 /") == 0


def test_long_chain():
    tokens = ["1"] + ["1", "+"] * 5000
    assert task.eval_rpn(tokens) == 5001


def test_deeply_nested():
    tokens = ["2"] * 5001 + ["*"] * 5000
    assert task.eval_rpn(tokens) == 2**5001


def test_empty_raises():
    with pytest.raises(ValueError):
        task.eval_rpn([])


@pytest.mark.parametrize("expr", ["+", "1 +", "1 2", "1 2 3 +", "1 2 + +"])
def test_malformed_raises(expr):
    with pytest.raises(ValueError):
        rpn(expr)
