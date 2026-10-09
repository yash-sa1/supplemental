# Module 1 — Big O Notation, Linear Search & Binary Search

## 1. What Big O actually measures

Big O describes **how the work grows as the input grows** — not how many
seconds something takes. We count "basic steps" (comparisons, assignments,
array reads) as a function of the input size `n`, then keep only the part
that dominates when `n` is huge.

```
f(n) = 3n² + 10n + 50      ->   O(n²)
```

At n = 1,000,000: `3n²` is 3×10¹², `10n` is 10⁷, `50` is 50. Only the n² term
matters, and the constant 3 doesn't change the *shape* of the growth.

### How fast do they grow?

| Big O        | Name         | n = 10 | n = 1,000   | n = 1,000,000        | Typical example                  |
|--------------|--------------|--------|-------------|----------------------|----------------------------------|
| `O(1)`       | constant     | 1      | 1           | 1                    | `arr[i]`, `dict[key]`, push/pop  |
| `O(log n)`   | logarithmic  | ~3     | ~10         | ~20                  | binary search                    |
| `O(n)`       | linear       | 10     | 1,000       | 1,000,000            | one loop, linear search          |
| `O(n log n)` | linearithmic | ~33    | ~10,000     | ~20,000,000          | good sorting (merge sort, `sorted`) |
| `O(n²)`      | quadratic    | 100    | 1,000,000   | 10¹² (too slow)      | nested loops over the same data  |
| `O(2ⁿ)`      | exponential  | 1,024  | 10³⁰¹       | forget it            | naive recursive Fibonacci, all subsets |
| `O(n!)`      | factorial    | 3.6M   | —           | —                    | all permutations                 |

Rule of thumb: Python does roughly **10⁷ simple steps per second**. So
n = 10⁵ with an O(n²) algorithm (10¹⁰ steps) takes ~15 minutes. That's why
the tests in this workbook use big inputs: they catch slow algorithms.

## 2. Rules for working it out

1. **Drop constants.** `O(2n)` → `O(n)`. `O(500)` → `O(1)`.
2. **Drop lower-order terms.** `O(n² + n)` → `O(n²)`.
3. **Sequential steps add.** Loop over `a`, then loop over `b` → `O(a + b)`.
4. **Nested steps multiply.** Loop over `a` with a loop over `b` inside → `O(a · b)`.
5. **Different inputs get different letters.** Two lists of sizes n and m are
   `O(n + m)`, not `O(n)` — you don't know which one is bigger.
6. **Halving (or doubling) each step → log.** If each step cuts the remaining
   problem in half, it takes log₂(n) steps to get to 1.
7. **Recursion: (number of calls) × (work per call).** Naive Fibonacci makes
   ~2ⁿ calls doing O(1) each → `O(2ⁿ)`.
8. **Count the hidden loops.** One line of Python can be O(n): `x in some_list`,
   `some_list.index(x)`, `arr[1:]` (slicing copies), `list.insert(0, x)`,
   `list.pop(0)`, `sum(arr)`, `max(arr)`, `"".join(...)`, `sorted(arr)` (n log n).

### Worked example

```python
def f(arr):
    n = len(arr)
    for i in range(n):          # n times
        for j in range(i, n):   #   n - i times
            ...                 #     O(1)
```

Total inner steps = n + (n-1) + ... + 1 = n(n+1)/2 → **O(n²)**. A shrinking inner
loop is still quadratic; it only halves the constant.

```python
def g(n):
    i = 1
    while i < n:
        i *= 2                  # 1, 2, 4, 8, ... reaches n after log2(n) steps
```

→ **O(log n)**.

## 3. Space complexity

The **extra** memory an algorithm uses, not counting the input (unless you
copy it).

- A few variables → `O(1)`.
- A new list/dict/set that grows with the input → `O(n)`.
- **Recursion uses the call stack**: each active call is a frame in memory.
  Recursing `n` deep → `O(n)` space even if you allocate nothing. Binary search
  written recursively → `O(log n)` space. (Python's default recursion limit is ~1000.)

## 4. Best, worst, average and amortised

- **Worst case** is the default meaning of "Big O" in exams unless told otherwise.
- **Best case**: linear search finds the target at index 0 → O(1). Rarely what's asked.
- **Average case**: hash table lookup is O(1) on average, O(n) worst case.
- **Amortised**: the average cost *per operation over a long sequence*.
  `list.append` occasionally copies the whole array to grow it (O(n)), but
  since capacity doubles each time, n appends cost O(n) total → **O(1) amortised**.

Formally: `O` is an upper bound, `Ω` (omega) a lower bound, `Θ` (theta) a tight
bound. Most people (and exams) say "O" when they mean the tight bound.

## 5. Python cost cheat-sheet

| Operation                              | Cost        |
|----------------------------------------|-------------|
| `len(x)`, `arr[i]`, `arr[i] = v`       | O(1)        |
| `arr.append(v)`, `arr.pop()`           | O(1) amortised |
| `arr.insert(0, v)`, `arr.pop(0)`       | **O(n)** — shifts everything |
| `v in arr`, `arr.index(v)`, `arr.count(v)` | O(n)    |
| `arr[a:b]` (slice)                     | O(b − a) — it **copies** |
| `sorted(arr)`, `arr.sort()`            | O(n log n)  |
| `v in set_`, `d[k]`, `d[k] = v`, `set_.add(v)` | O(1) average |
| `s1 + s2` (strings)                    | O(len(s1) + len(s2)) — strings are immutable |
| building a string with `+=` in a loop  | up to O(n²) — use `"".join(parts)` |

## 6. Linear search

Check each element in turn until you find the target.

- Works on **any** sequence, sorted or not.
- Time: best O(1), worst O(n). Space: O(1).
- Return as soon as you find a match (for "first occurrence").
- Classic bug: `if result:` treats index `0` as "not found". Compare with `-1`.

## 7. Binary search

Only works on **sorted** data. Look at the middle element; the sorted order
tells you which half can't contain the target, so throw that half away.

```
target = 23
[ 2  5  8  12  16  23  38  56  72  91 ]
  lo             mid                hi     16 < 23 -> go right
                     [23  38  56  72  91 ]
                      lo      mid     hi   56 > 23 -> go left
                     [23  38]
                      lo/mid hi            23 == 23 -> found at index 5
```

Each step halves the search space → at most ⌊log₂ n⌋ + 1 steps.
1,000,000 elements → ~20 comparisons.

### The template (closed interval `[lo, hi]`)

```text
lo = 0, hi = n - 1
while lo <= hi:                # interval still has at least one element
    mid = (lo + hi) // 2
    if arr[mid] == target: found
    elif arr[mid] < target: lo = mid + 1    # discard mid and everything left of it
    else:                   hi = mid - 1    # discard mid and everything right of it
not found
```

The **invariant**: "if the target is anywhere, it's inside `[lo, hi]`". Every
update must keep that true AND shrink the interval (that's why it's `mid + 1`
/ `mid - 1`, never just `mid` in this version — otherwise it can loop forever).

### Variations you need to know

| Variation | Idea | Task |
|---|---|---|
| **Exact match** | the template above | t03 |
| **Recursive** | same logic, pass `lo`/`hi` as parameters; base case `lo > hi` | t03 |
| **First / last occurrence** | on a match, *record it and keep going* left (or right) | t05 |
| **Lower bound / insertion point** | smallest index with `arr[i] >= target` (Python: `bisect.bisect_left`) | t05 |
| **Rotated / partially sorted** | decide which half is sorted, then whether the target is in it | t06 |
| **Search on a slope** | compare `arr[mid]` with `arr[mid+1]` to know which way is "up" | t07 |
| **Binary search on the answer** | answer lies in a range and "is `x` good enough?" is monotonic (false…false true…true); binary search for the first true | t04, t09 |
| **Partition search** | binary search *where to cut* rather than a value | t08 |

### Pitfalls

- `while lo < hi` vs `while lo <= hi`: pick one template and know why.
  `lo <= hi` pairs with `hi = mid - 1`; `lo < hi` pairs with `hi = mid`.
- `lo = mid` (without `+ 1`) with `mid = (lo + hi) // 2` can loop forever when
  `hi == lo + 1`.
- **Don't slice** (`binary_search(arr[mid:])`): slicing copies, making it O(n).
  Pass indices. (The tests use a `ProbeArray` that refuses slicing and counts reads.)
- In Java/C++, `(lo + hi) / 2` can overflow; they write `lo + (hi - lo) / 2`.
  Python ints don't overflow, but examiners like the question.
- Empty array: `hi = -1`, the loop never runs, return -1. Make sure your code agrees.

## 8. Implementation walkthroughs (the stuff exams ask you to write)

Every code block below runs as-is (the `assert` lines are examples you can
try yourself). Learn these until you can write them from memory.

### 8.1 Linear search and its variants

```python
def linear_search(arr, target):
    """Index of the FIRST occurrence of target, or -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i          # stop as soon as it's found
    return -1                 # only after checking everything


def linear_search_last(arr, target):
    """Index of the LAST occurrence: walk backwards."""
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            return i
    return -1


def find_all(arr, target):
    """Every index where target appears."""
    return [i for i, x in enumerate(arr) if x == target]


def find_max(arr):
    """Largest value — the same 'look at everything once' idea."""
    if not arr:
        raise ValueError("max of empty sequence")
    best = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > best:
            best = arr[i]
    return best


assert linear_search([4, 2, 7, 2], 2) == 1
assert linear_search([4, 2, 7], 5) == -1
assert linear_search_last([4, 2, 7, 2], 2) == 3
assert find_all([4, 2, 7, 2], 2) == [1, 3]
assert find_max([3, -1, 9, 4]) == 9
```

| Function | Best | Worst | Space |
|---|---|---|---|
| `linear_search` | O(1) (first element) | O(n) (last / missing) | O(1) |
| `find_all`, `find_max` | O(n) | O(n) | O(k) / O(1) |

### 8.2 Binary search — iterative

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1          # search the CLOSED range [lo, hi]
    while lo <= hi:                   # range not empty
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1              # target can only be right of mid
        else:
            hi = mid - 1              # target can only be left of mid
    return -1


assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
assert binary_search([], 1) == -1
```

**Trace** — `arr = [-1, 0, 3, 5, 9, 12]`, `target = 9`:

| step | lo | hi | mid | arr[mid] | action |
|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 3  | 3 < 9 → `lo = 3` |
| 2 | 3 | 5 | 4 | 9  | found → return 4 |

**Trace** — `target = 2` (missing):

| step | lo | hi | mid | arr[mid] | action |
|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 3  | 3 > 2 → `hi = 1` |
| 2 | 0 | 1 | 0 | -1 | -1 < 2 → `lo = 1` |
| 3 | 1 | 1 | 1 | 0  | 0 < 2 → `lo = 2` |
| 4 | 2 | 1 | — | —  | `lo > hi`, range empty → return -1 |

Time O(log n), space O(1).

### 8.3 Binary search — recursive

```python
def binary_search_recursive(arr, target, lo=0, hi=None):
    if hi is None:                    # first call: search the whole array
        hi = len(arr) - 1
    if lo > hi:                       # base case: empty range
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    return binary_search_recursive(arr, target, lo, mid - 1)


assert binary_search_recursive([1, 3, 5, 7, 9], 7) == 3
assert binary_search_recursive([1, 3, 5, 7, 9], 4) == -1
```

Time O(log n), space **O(log n)** — one stack frame per halving.
Never write `binary_search_recursive(arr[mid+1:], target)`: the slice copies
half the array every call (O(n) total) and the returned index is relative to
the slice, not the original.

### 8.4 First / last occurrence, lower & upper bound

With duplicates, "find any match" isn't enough. The trick: **when you find a
match, remember it and keep searching** in the direction you care about.

```python
def first_occurrence(arr, target):
    lo, hi, found = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            found = mid
            hi = mid - 1              # there may be an earlier one
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return found


def last_occurrence(arr, target):
    lo, hi, found = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            found = mid
            lo = mid + 1              # there may be a later one
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return found


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    return 0 if first == -1 else last_occurrence(arr, target) - first + 1


def lower_bound(arr, target):
    """First index i with arr[i] >= target (== len(arr) if none).
    Also the index where target should be INSERTED to keep arr sorted."""
    lo, hi = 0, len(arr)              # half-open range [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid                  # mid might be the answer: keep it
    return lo


def upper_bound(arr, target):
    """First index i with arr[i] > target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


data = [1, 2, 2, 2, 5, 7]
assert first_occurrence(data, 2) == 1
assert last_occurrence(data, 2) == 3
assert count_occurrences(data, 2) == 3
assert count_occurrences(data, 4) == 0
assert lower_bound(data, 2) == 1 and upper_bound(data, 2) == 4
assert lower_bound(data, 4) == 4      # 4 would be inserted before 5
assert lower_bound(data, 99) == 6     # after everything

import bisect                          # Python's built-in versions:
assert bisect.bisect_left(data, 2) == lower_bound(data, 2)
assert bisect.bisect_right(data, 2) == upper_bound(data, 2)
```

Two loop styles, don't mix them up:

| Style | Range | Loop | Shrink |
|---|---|---|---|
| closed | `[lo, hi]`, `hi = n - 1` | `while lo <= hi` | `lo = mid + 1` / `hi = mid - 1` |
| half-open | `[lo, hi)`, `hi = n` | `while lo < hi` | `lo = mid + 1` / `hi = mid` |

### 8.5 Binary search on the answer

When the answer is a number in a range and a yes/no question about it flips
**once** (no, no, no, yes, yes…), binary search for the first "yes" (or last "no").

```python
def first_true(lo, hi, is_ok):
    """Smallest x in [lo, hi] with is_ok(x) True (is_ok must be monotonic).
    Returns hi + 1 if none."""
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_ok(mid):
            hi = mid - 1              # mid works; look for something smaller
        else:
            lo = mid + 1
    return lo


def int_sqrt(x):
    """floor(sqrt(x)) without ** or math: largest r with r*r <= x."""
    # first r where r*r > x, minus one
    return first_true(0, x + 1, lambda r: r * r > x) - 1


assert [int_sqrt(v) for v in [0, 1, 3, 4, 8, 9, 10**18]] == [0, 1, 1, 2, 2, 3, 10**9]
```

Classic uses: square root, "minimum speed to finish in time" (Koko eating
bananas), "minimum ship capacity in D days", "split array largest sum".

### 8.6 Search in a rotated sorted array

`[4, 5, 6, 7, 0, 1, 2]` — cut anywhere and **one half is always sorted**.
Check if the target sits inside the sorted half's range; if not, it's in the other half.

```python
def search_rotated(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:                   # left half sorted
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                     # right half sorted
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated([1], 1) == 0
```

### 8.7 Working out the Big O of recursive code

Write the cost as a **recurrence**: T(n) = (cost of the recursive calls) + (work done in this call).

| Recurrence | Example | Result |
|---|---|---|
| T(n) = T(n−1) + O(1) | recursive sum/factorial, linked-list recursion | O(n) |
| T(n) = T(n−1) + O(n) | recursive selection sort, `f(arr[1:])` (slice copies) | O(n²) |
| T(n) = T(n/2) + O(1) | binary search | O(log n) |
| T(n) = T(n/2) + O(n) | quickselect (average) | O(n) |
| T(n) = 2T(n/2) + O(1) | tree traversal (balanced) | O(n) |
| T(n) = 2T(n/2) + O(n) | merge sort | O(n log n) |
| T(n) = 2T(n−1) + O(1) | naive Fibonacci, towers of Hanoi | O(2ⁿ) |

Picture the **recursion tree**: total = (number of calls) × (work per call),
summed level by level. Space = the **deepest** chain of calls alive at once.

```python
def power(base, exp):
    """Fast exponentiation: T(n) = T(n/2) + O(1) -> O(log exp)."""
    if exp == 0:
        return 1
    half = power(base, exp // 2)      # ONE recursive call, reused
    return half * half if exp % 2 == 0 else half * half * base


assert power(2, 10) == 1024 and power(3, 0) == 1
# Calling power(base, exp // 2) TWICE instead of reusing `half` makes it
# T(n) = 2T(n/2) + O(1) = O(n) — a classic exam trap.
```

### 8.8 Linear vs binary: when is sorting first worth it?

- One search in unsorted data: linear, O(n). Sorting first (O(n log n)) is slower.
- k searches: linear costs O(k·n); sort once + binary search costs O(n log n + k log n).
  Worth it once k is bigger than about log n.
- Lots of lookups and no need for order? A **set/dict** gives O(1) average (Module 4).

## 9. Tasks

| #  | Task                                   | Difficulty | LeetCode | File |
|----|----------------------------------------|------------|----------|------|
| 01 | Big O Quiz (17 snippets)               | Easy       | —        | `tasks/t01_easy_big_o_quiz.py` |
| 02 | Linear Search                          | Easy       | —        | `tasks/t02_easy_linear_search.py` |
| 03 | Binary Search (iterative + recursive)  | Easy       | 704      | `tasks/t03_easy_binary_search.py` |
| 04 | Integer Square Root                    | Easy       | 69       | `tasks/t04_easy_sqrt_floor.py` |
| 05 | First and Last Position                | Medium     | 34       | `tasks/t05_medium_search_range.py` |
| 06 | Search in Rotated Sorted Array         | Medium     | 33       | `tasks/t06_medium_search_rotated.py` |
| 07 | Find Peak Element                      | Medium     | 162      | `tasks/t07_medium_find_peak.py` |
| 08 | Median of Two Sorted Arrays            | Hard       | 4        | `tasks/t08_hard_median_two_sorted.py` |
| 09 | Split Array Largest Sum                | Hard       | 410      | `tasks/t09_hard_split_array.py` |

```bash
pytest m01_big_o                                          # whole module
pytest m01_big_o/tests/test_t03_easy_binary_search.py     # one task
pytest m01_big_o/tests/test_t03_easy_binary_search.py -x  # stop at first failure
python progress.py m01                                    # dashboard
```

Several tests pass your function a `ProbeArray` (from `common/probes.py`)
instead of a list. It behaves like a read-only list but counts every `arr[i]`
read, so a "binary search" that secretly scans the array fails with a message
like `Read 1000000 elements ... binary search needs ~20`.
