import random

from common.loader import load_task
from m02_linked_lists.framework import from_list, to_list

task = load_task(__file__)


def digits(number):
    return [int(d) for d in reversed(str(number))]


def add(a, b):
    return to_list(task.add_two_numbers(from_list(digits(a)), from_list(digits(b))))


def test_example_1():
    assert to_list(task.add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))) == [7, 0, 8]


def test_example_2_zeros():
    assert add(0, 0) == [0]


def test_example_3_carry_ripples_past_shorter_list():
    assert to_list(task.add_two_numbers(from_list([9, 9, 9, 9]), from_list([9, 9]))) == [8, 9, 0, 0, 1]


def test_final_carry_creates_new_digit():
    assert add(5, 5) == [0, 1]
    assert add(999, 1) == [0, 0, 0, 1]


def test_first_shorter():
    assert add(1, 1000) == digits(1001)


def test_second_shorter():
    assert add(1000, 1) == digits(1001)


def test_adding_zero():
    assert add(12345, 0) == digits(12345)
    assert add(0, 12345) == digits(12345)


def test_single_digits_no_carry():
    assert add(3, 4) == [7]


def test_inputs_not_modified():
    l1, l2 = from_list([2, 4, 3]), from_list([5, 6, 4])
    task.add_two_numbers(l1, l2)
    assert to_list(l1) == [2, 4, 3]
    assert to_list(l2) == [5, 6, 4]


def test_randomized():
    rng = random.Random(2)
    for _ in range(300):
        a, b = rng.randint(0, 10**12), rng.randint(0, 10**6)
        assert add(a, b) == digits(a + b), f"{a} + {b}"


def test_huge_numbers():
    # 100,000-digit numbers
    rng = random.Random(22)
    a = [rng.randint(0, 9) for _ in range(99_999)] + [rng.randint(1, 9)]
    b = [9] * 100_000
    result = to_list(task.add_two_numbers(from_list(a), from_list(b)))
    assert len(result) in (100_000, 100_001)
    # a + (10^100000 - 1) = a - 1 + 10^100000: check the low digits
    expected_low = []
    borrow = 1
    for d in a[:10]:
        d -= borrow
        borrow = 1 if d < 0 else 0
        expected_low.append(d % 10)
    assert result[:10] == expected_low
    assert result[-1] == 1
