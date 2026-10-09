import random
from collections import Counter

from common.loader import load_task

task = load_task(__file__)


def brute(s, t):
    if not t:
        return ""
    need = Counter(t)
    for length in range(len(t), len(s) + 1):
        for i in range(len(s) - length + 1):
            window = Counter(s[i : i + length])
            if all(window[c] >= n for c, n in need.items()):
                return s[i : i + length]
    return ""


def test_example_1():
    assert task.min_window("ADOBECODEBANC", "ABC") == "BANC"


def test_example_2():
    assert task.min_window("a", "a") == "a"


def test_example_3_not_enough_duplicates():
    assert task.min_window("a", "aa") == ""


def test_empty_t():
    assert task.min_window("abc", "") == ""


def test_empty_s():
    assert task.min_window("", "a") == ""


def test_t_longer_than_s():
    assert task.min_window("ab", "abc") == ""


def test_whole_string_is_window():
    assert task.min_window("abc", "cba") == "abc"


def test_duplicates_in_t():
    assert task.min_window("aaflslflsldkalskaaa", "aaa") == "aaa"
    assert task.min_window("abbbba", "aa") == "abbbba"


def test_case_sensitive():
    assert task.min_window("aA", "A") == "A"
    assert task.min_window("abc", "C") == ""


def test_leftmost_on_ties():
    assert task.min_window("abXba", "ab") == "ab"


def test_window_at_end():
    assert task.min_window("xxxxab", "ba") == "ab"


def test_randomized_against_brute_force():
    rng = random.Random(76)
    for _ in range(400):
        s = "".join(rng.choice("abc") for _ in range(rng.randint(0, 12)))
        t = "".join(rng.choice("abc") for _ in range(rng.randint(0, 4)))
        assert task.min_window(s, t) == brute(s, t), f"s={s!r}, t={t!r}"


def test_large_input():
    s = "a" * 50_000 + "b" + "a" * 50_000 + "c"
    assert task.min_window(s, "bc") == "b" + "a" * 50_000 + "c"


def test_large_t():
    rng = random.Random(760)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(rng.choice(alphabet) for _ in range(100_000))
    t = s[40_000:60_000]
    result = task.min_window(s, t)
    need, have = Counter(t), Counter(result)
    assert all(have[c] >= n for c, n in need.items())
    assert len(result) <= 20_000
