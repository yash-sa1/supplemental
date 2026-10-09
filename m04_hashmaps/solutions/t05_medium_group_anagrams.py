"""
Task 05 · Medium · Group Anagrams  (SOLUTION)

All anagrams share the same sorted letters, so "".join(sorted(word)) is a
perfect grouping key. (A tuple of 26 letter counts also works for a-z only.)
Lists can't be dict keys (unhashable) — strings and tuples can.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in strs:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
