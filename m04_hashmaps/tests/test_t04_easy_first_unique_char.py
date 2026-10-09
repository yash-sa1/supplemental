import random
import string

from common.loader import load_task

task = load_task(__file__)


def brute(s):
    for i, ch in enumerate(s):
        if s.count(ch) == 1:
            return i
    return -1


def test_example_1():
    assert task.first_uniq_char("leetcode") == 0


def test_example_2():
    assert task.first_uniq_char("loveleetcode") == 2


def test_example_3_none_unique():
    assert task.first_uniq_char("aabb") == -1


def test_empty():
    assert task.first_uniq_char("") == -1


def test_single_char():
    assert task.first_uniq_char("z") == 0


def test_unique_is_last():
    assert task.first_uniq_char("aabbc") == 4


def test_repeat_appears_much_later():
    # 'a' looks unique until the very end
    assert task.first_uniq_char("abcdefa") == 1


def test_case_sensitive():
    assert task.first_uniq_char("aA") == 0


def test_randomized():
    rng = random.Random(387)
    for _ in range(500):
        s = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 10)))
        assert task.first_uniq_char(s) == brute(s), f"s={s!r}"


def test_long_string_unique_at_end():
    # many distinct repeated chars so s.count() per char is genuinely O(n^2)
    body = (string.ascii_letters * 4000)
    s = body + body + "!"
    assert task.first_uniq_char(s) == len(s) - 1
