import random

from common.loader import load_task

task = load_task(__file__)


def canon(groups):
    """Order-insensitive form: sort inside each group, then sort the groups."""
    return sorted(sorted(g) for g in groups)


def test_example_1():
    result = task.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert canon(result) == canon([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])


def test_example_2_empty_string():
    assert canon(task.group_anagrams([""])) == [[""]]


def test_example_3_no_strings():
    assert task.group_anagrams([]) == []


def test_single_word():
    assert canon(task.group_anagrams(["a"])) == [["a"]]


def test_duplicates_kept():
    assert canon(task.group_anagrams(["a", "a"])) == [["a", "a"]]


def test_no_anagrams():
    assert canon(task.group_anagrams(["abc", "def", "ghi"])) == [["abc"], ["def"], ["ghi"]]


def test_same_letters_different_counts_are_different_groups():
    assert canon(task.group_anagrams(["aab", "abb", "bab"])) == [["aab"], ["abb", "bab"]]


def test_different_lengths():
    assert canon(task.group_anagrams(["a", "aa", "aaa", "a"])) == [["a", "a"], ["aa"], ["aaa"]]


def test_multiple_empty_strings():
    assert canon(task.group_anagrams(["", "", "b"])) == [["", ""], ["b"]]


def test_returns_list_of_lists():
    result = task.group_anagrams(["ab", "ba"])
    assert isinstance(result, list) and all(isinstance(g, list) for g in result)


def test_does_not_mutate_input():
    strs = ["eat", "tea", "tan"]
    task.group_anagrams(strs)
    assert strs == ["eat", "tea", "tan"]


def test_randomized():
    rng = random.Random(49)
    for _ in range(200):
        strs = ["".join(rng.choice("abc") for _ in range(rng.randint(0, 3))) for _ in range(rng.randint(0, 12))]
        buckets = {}
        for s in strs:
            buckets.setdefault("".join(sorted(s)), []).append(s)
        assert canon(task.group_anagrams(strs)) == canon(buckets.values()), f"strs={strs}"


def test_large_input():
    rng = random.Random(490)
    words = ["".join(rng.choice("abcdefghij") for _ in range(8)) for _ in range(500)]
    strs = ["".join(rng.sample(w, len(w))) for w in words for _ in range(20)]  # 10,000 strings
    result = task.group_anagrams(strs)
    assert sum(len(g) for g in result) == 10_000
    for g in result:
        assert len({"".join(sorted(s)) for s in g}) == 1
