"""
Task 02 · Easy · Linear Search  (SOLUTION)
"""
from collections.abc import Sequence
from typing import Any


def linear_search(arr: Sequence, target: Any) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # first match: return immediately
    return -1
