import pytest

from common.loader import load_task
from common.probes import ProbeArray

task = load_task(__file__)


def search(values, target):
    return task.linear_search(ProbeArray(values), target)


def test_example_found():
    assert search([4, 2, 7, 2], 2) == 1


def test_example_not_found():
    assert search([4, 2, 7], 5) == -1


def test_empty_array():
    assert search([], 1) == -1


def test_single_element_found():
    assert search([9], 9) == 0


def test_single_element_not_found():
    assert search([9], 8) == -1


def test_target_at_first_index():
    assert search([3, 1, 2], 3) == 0


def test_target_at_last_index():
    assert search([3, 1, 2], 2) == 2


def test_duplicates_return_first_occurrence():
    assert search([5, 5, 5, 5], 5) == 0
    assert search([1, 2, 3, 2, 1], 1) == 0


def test_negative_numbers_and_zero():
    assert search([-3, 0, -1], 0) == 1
    assert search([-3, 0, -1], -1) == 2


def test_unsorted_input():
    assert search([10, -4, 99, 3, 0], 3) == 3


def test_strings():
    assert search(["b", "a", "c"], "c") == 2
    assert search(["b", "a", "c"], "z") == -1


def test_none_as_target():
    assert search([1, None, 2], None) == 1


def test_zero_is_not_confused_with_false_or_missing():
    # A common bug: `if result:` treats index 0 as "not found".
    assert search([0, 1], 0) == 0


@pytest.mark.parametrize("target_index", [0, 1, 500, 999])
def test_stops_at_first_match(target_index):
    arr = ProbeArray(range(1000))
    assert task.linear_search(arr, target_index) == target_index
    assert arr.reads <= target_index + 1, (
        f"Read {arr.reads} elements to find index {target_index}; "
        "you should stop as soon as you find it"
    )


def test_large_not_found_reads_each_element_once():
    arr = ProbeArray(range(100_000))
    assert task.linear_search(arr, -1) == -1
    assert arr.reads <= 100_000, f"Read {arr.reads} elements; each should be read at most once"
