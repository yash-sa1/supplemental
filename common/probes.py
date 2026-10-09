"""Instrumented containers used by tests to check time complexity, not just correctness."""
from collections.abc import Iterable


class ProbeArray:
    """
    A read-only list stand-in that counts how many elements you read.

    Supports len(arr), arr[i] (including negative i) and iteration.
    Every element read increments .reads, so a test can assert that a
    "binary search" really only looked at ~log2(n) elements.

    Slicing (arr[a:b]) raises TypeError on purpose: a slice copies the
    elements, which is O(n) and defeats the point of binary search.
    Pass indices (lo, hi) around instead.
    """

    def __init__(self, values: Iterable):
        self._data = list(values)
        self.reads = 0

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise TypeError(
                "Slicing copies the array (O(n)). Track lo/hi indices instead of slicing."
            )
        self.reads += 1
        return self._data[index]

    def __iter__(self):
        for i in range(len(self._data)):
            yield self[i]

    def __repr__(self) -> str:
        preview = self._data if len(self._data) <= 10 else self._data[:10] + ["..."]
        return f"ProbeArray({preview}, len={len(self._data)})"
