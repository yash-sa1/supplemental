# Module 4 — Hash Maps & Hash Sets

## 1. The idea

A hash map stores **key → value** pairs with (average) **O(1)** insert,
lookup and delete. The trick: turn the key into an array index.

```
key "cat" ──hash()──▶ 7_294_018_331 ──% 8──▶ bucket 3

buckets (capacity 8):
  0: []
  1: [("dog", 4)]
  2: []
  3: [("cat", 1), ("act", 7)]     ◀ collision: both hashed to 3, chained in a list
  4: []
  5: [("owl", 2)]
  6: []
  7: []
```

1. A **hash function** maps a key to a (big) integer. Same key → same number, always.
2. `index = hash(key) % capacity` picks a **bucket**.
3. Look only in that bucket, comparing keys with `==`.

A **hash set** is the same thing with keys only (no values): "have I seen this?" in O(1).

## 2. Collisions

Different keys can land in the same bucket (there are infinitely many keys and
only `capacity` buckets). Two classic fixes:

**Separate chaining** — each bucket is a list of entries; collisions just
append. Simple, what you'll build in t01.

**Open addressing** — one entry per slot; on a collision, probe for another
slot: linear probing (`i+1, i+2, …`), quadratic probing, double hashing.
Deletion needs "tombstone" markers so later probes don't stop early.
CPython's `dict` uses open addressing.

## 3. Load factor and resizing

**Load factor α = (number of entries) / (number of buckets).**
As α grows, chains get longer and lookups slow down. So when α passes a
threshold (0.75 is common), **allocate twice as many buckets and re-insert
every entry** (the bucket index depends on capacity, so everything moves).

A resize costs O(n), but because capacity **doubles**, resizes get rarer
as the map grows: n inserts cost O(n) total → **amortised O(1)** per insert
(the same argument as `list.append`).

## 4. Complexity

| Operation            | Average | Worst case |
|----------------------|---------|------------|
| insert / update      | O(1)*   | O(n)       |
| lookup / `in`        | O(1)    | O(n)       |
| delete               | O(1)    | O(n)       |
| iterate everything   | O(n + capacity) | |

\* amortised, because of resizing.
Worst case happens when many keys collide into one bucket (bad hash function,
or deliberately crafted keys) — it degrades to a linked-list search.

Space: O(n).

## 5. What can be a key? (hashability)

A key must be **hashable**: `hash(key)` must never change while it's in the map,
and **`a == b` must imply `hash(a) == hash(b)`**.

- Hashable: `int`, `float`, `str`, `bool`, `None`, `tuple` (of hashables), `frozenset`.
- **Not** hashable: `list`, `dict`, `set` — they're mutable. If you changed a list
  after using it as a key, its hash would change and you'd never find it again.
  Convert: `tuple(my_list)`, `frozenset(my_set)`, `"".join(sorted(word))`.
- Because `1 == 1.0 == True` and they hash equal, they're the **same key** in a dict.
- Custom classes: define `__eq__` and `__hash__` together (hash the same fields you compare).

## 6. Python toolbox

```python
d = {}
d["a"] = 1                 # insert / overwrite
d["a"]                     # KeyError if missing
d.get("b", 0)              # default instead of KeyError
"a" in d                   # O(1) membership (keys)
del d["a"]                 # KeyError if missing
d.pop("a", None)           # remove, no error if missing
d.setdefault("k", []).append(x)   # grouping idiom
for k, v in d.items(): ... # dicts keep insertion order (Python 3.7+)

s = set(); s.add(x); x in s; s.discard(x)
a | b, a & b, a - b        # union, intersection, difference

from collections import defaultdict, Counter
groups = defaultdict(list); groups[key].append(x)   # no KeyError, auto-creates []
counts = Counter("banana")                          # {'a': 3, 'n': 2, 'b': 1}
```

Some tasks here ban `Counter`/`OrderedDict` so you practise building the logic
yourself — in an exam, ask whether they're allowed.

## 7. Patterns (these solve a huge share of interview/exam questions)

| Pattern | Question it answers | Example |
|---|---|---|
| **Frequency count** | "how many times does each thing appear?" | anagram (t03), first unique (t04), top-k (t06) |
| **Seen set** | "have I seen this before?" | duplicates, cycle detection by memory |
| **Complement lookup** | "is the partner I need already here?" `target - x in seen` | two sum (t02) |
| **Canonical key grouping** | "which items are equivalent?" key = sorted word / tuple of counts | group anagrams (t05) |
| **Set for O(1) neighbours** | "is x+1 present?" | longest consecutive (t07) |
| **Prefix sum + map** | "how many subarrays sum to k?" count earlier prefixes equal to `prefix − k` | t08 |
| **Sliding window + counts** | "smallest/longest window satisfying a character condition" | min window substring (t10) |
| **Map + linked list** | O(1) lookup **and** O(1) reordering | LRU cache (t09) |
| **Bucket sort by frequency** | top-k without a full sort | t06 |

Typical upgrade: a nested loop that *searches* for something (O(n²)) becomes
one loop plus a hash map lookup (O(n)) — trading O(n) memory for time.

## 8. Pitfalls

- **Mutating a key** after insertion (only possible with custom mutable objects) → lost entry.
- Checking `if d[key]:` when the stored value might be `0`/`None`/`""` — use `key in d`.
- Iterating a dict **while adding/removing keys** → `RuntimeError`. Iterate over `list(d)`.
- Forgetting the **empty prefix** (`{0: 1}`) in prefix-sum problems.
- Two sum: insert **after** checking, or an element pairs with itself.
- In your own hash map: forgetting to **rehash on resize** (old bucket indices
  are wrong for the new capacity), or letting an overwrite increase the size.
- Hash order isn't sorted order: never rely on iteration order for correctness
  unless the problem says so.

## 9. Implementation walkthroughs (the stuff exams ask you to write)

Every code block below runs as-is, top to bottom (the `assert` lines are examples).

### 9.1 Writing a hash function

A hash function turns a key into an integer, then **compression** (`% capacity`)
turns that into a bucket index. For strings, the classic is a
**polynomial rolling hash**: treat the characters as digits in base 31.

```python
def string_hash(s, base=31, mod=2**32):
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod    # like reading a number digit by digit
    return h


def bucket_index(key, capacity):
    return string_hash(key) % capacity


assert string_hash("abc") == (97 * 31**2 + 98 * 31 + 99)
assert string_hash("abc") != string_hash("cba")    # order matters (a plain sum wouldn't care)
assert 0 <= bucket_index("hello", 8) < 8
```

What makes a good hash function:
- **Deterministic**: same key → same hash, every time.
- **Uniform**: spreads keys evenly over the buckets (fewer collisions).
- **Fast** to compute.
- Uses **all** of the key: "sum of character codes" is bad because every
  anagram collides (`"abc"`, `"cab"`…).

In Python you just call the built-in `hash(key)`. (String hashes are randomised
per process for security, so don't rely on the actual numbers.)

### 9.2 Hash map with separate chaining (+ resizing)

```python
class ChainingHashMap:
    def __init__(self, capacity=8, max_load=0.75):
        self._buckets = [[] for _ in range(capacity)]   # NOT [[]] * capacity (same list 8 times!)
        self._size = 0
        self._max_load = max_load

    def _bucket(self, key):
        return self._buckets[hash(key) % len(self._buckets)]

    def put(self, key, value):                 # O(1) average
        bucket = self._bucket(key)
        for pair in bucket:
            if pair[0] == key:                 # key already there: overwrite
                pair[1] = value
                return
        bucket.append([key, value])            # new key: chain it
        self._size += 1
        if self._size / len(self._buckets) > self._max_load:
            self._resize()

    def get(self, key, default=None):          # O(1) average
        for k, v in self._bucket(key):
            if k == key:
                return v
        return default

    def remove(self, key):                     # O(1) average
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def _resize(self):                         # O(n), but rare -> amortised O(1)
        old = self._buckets
        self._buckets = [[] for _ in range(2 * len(old))]
        for bucket in old:
            for k, v in bucket:                # re-hash: index depends on capacity
                self._bucket(k).append([k, v])

    def __len__(self):
        return self._size

    def __contains__(self, key):
        return any(k == key for k, _ in self._bucket(key))


m = ChainingHashMap()
for i in range(100):
    m.put(f"key{i}", i)
m.put("key5", 500)                             # overwrite
assert m.get("key5") == 500 and len(m) == 100
assert m.remove("key5") and "key5" not in m and m.get("key5") is None
assert len(m._buckets) == 256                  # grew 8 -> 16 -> ... -> 256
```

### 9.3 Hash map with open addressing (linear probing)

One entry per slot. On a collision, try the next slot (`i + 1`, wrapping).
Deleting needs a **tombstone**: if you emptied the slot, a later search would
stop there and miss keys that probed past it.

```python
_EMPTY = object()        # never used
_DELETED = object()      # tombstone: "keep probing past me"


class LinearProbingHashMap:
    def __init__(self, capacity=8):
        self._keys = [_EMPTY] * capacity
        self._values = [None] * capacity
        self._size = 0

    def _probe(self, key):
        """Yield slot indices in probe order, starting at the home slot."""
        cap = len(self._keys)
        start = hash(key) % cap
        for step in range(cap):
            yield (start + step) % cap

    def put(self, key, value):
        if (self._size + 1) / len(self._keys) > 0.5:   # probing needs a low load factor
            self._resize()
        first_tombstone = None
        for i in self._probe(key):
            k = self._keys[i]
            if k is _EMPTY:                              # key isn't present: insert
                target = first_tombstone if first_tombstone is not None else i
                self._keys[target], self._values[target] = key, value
                self._size += 1
                return
            if k is _DELETED:
                if first_tombstone is None:
                    first_tombstone = i                  # reuse the first free-ish slot
            elif k == key:                               # found: overwrite
                self._values[i] = value
                return
        # table full of tombstones: reuse one
        self._keys[first_tombstone], self._values[first_tombstone] = key, value
        self._size += 1

    def get(self, key, default=None):
        for i in self._probe(key):
            k = self._keys[i]
            if k is _EMPTY:
                return default                           # a truly empty slot ends the search
            if k is not _DELETED and k == key:
                return self._values[i]
        return default

    def remove(self, key):
        for i in self._probe(key):
            k = self._keys[i]
            if k is _EMPTY:
                return False
            if k is not _DELETED and k == key:
                self._keys[i], self._values[i] = _DELETED, None
                self._size -= 1
                return True
        return False

    def _resize(self):
        old = [(k, v) for k, v in zip(self._keys, self._values)
               if k is not _EMPTY and k is not _DELETED]
        self._keys = [_EMPTY] * (2 * len(self._keys))   # tombstones are dropped here
        self._values = [None] * len(self._keys)
        self._size = 0
        for k, v in old:
            self.put(k, v)

    def __len__(self):
        return self._size


lp = LinearProbingHashMap()
for k in [8, 16, 24]:            # hash(int) == int, so all three start at slot 0 of 8
    lp.put(k, str(k))            # -> they land in slots 0, 1, 2
assert lp.get(24) == "24"
lp.remove(16)                    # slot 1 becomes a tombstone, not empty
assert lp.get(24) == "24"        # still found: probing continues past the tombstone
lp.put(32, "32")
assert lp.get(32) == "32" and len(lp) == 3 and lp.get(16) is None
```

**Probe trace** (capacity 8, keys 8, 16, 24 all hash to slot 0):
```
put 8   -> slot 0 empty                         [8 , _ , _ , ...]
put 16  -> slot 0 taken, try 1: empty           [8 , 16, _ , ...]
put 24  -> slots 0, 1 taken, try 2: empty       [8 , 16, 24, ...]
del 16  -> slot 1 = TOMBSTONE                   [8 , ☠ , 24, ...]
get 24  -> 0: 8 no, 1: ☠ keep going, 2: found   (an EMPTY slot 1 would have stopped the search)
```

Chaining vs open addressing:

| | Separate chaining | Open addressing |
|---|---|---|
| Collisions | append to the bucket's list | probe for another slot |
| Load factor | can exceed 1 | must stay < 1 (usually ≤ 0.5–0.7) |
| Delete | just remove from the list | needs tombstones |
| Memory | extra list/node per entry | one flat array (cache-friendly) |

### 9.4 Hash set

A set is a map that only stores keys.

```python
class HashSet:
    def __init__(self):
        self._map = ChainingHashMap()

    def add(self, key):
        self._map.put(key, True)

    def remove(self, key):
        return self._map.remove(key)

    def __contains__(self, key):
        return key in self._map

    def __len__(self):
        return len(self._map)


hs = HashSet()
for x in [3, 1, 3, 2, 1]:
    hs.add(x)
assert len(hs) == 3 and 2 in hs and 9 not in hs
```

### 9.5 Counting frequencies (three ways)

```python
from collections import Counter, defaultdict


def count_plain(items):
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1     # get() with a default avoids KeyError
    return counts


def count_defaultdict(items):
    counts = defaultdict(int)                # missing keys start at int() == 0
    for x in items:
        counts[x] += 1
    return dict(counts)


word = "mississippi"
assert count_plain(word) == count_defaultdict(word) == dict(Counter(word))
assert Counter(word).most_common(1) == [("i", 4)]
```

### 9.6 Contains duplicate / first repeated element (seen-set)

```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


def first_repeated(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    return None


assert contains_duplicate([1, 2, 3, 1]) and not contains_duplicate([1, 2, 3])
assert first_repeated([5, 3, 4, 3, 5]) == 3
# One-liner version: len(set(nums)) != len(nums)
```

O(n) time, O(n) space — versus O(n²) comparing every pair, or O(n log n) sorting first.

### 9.7 Two sum (complement lookup)

```python
def two_sum(nums, target):
    index_of = {}                        # value -> index where we saw it
    for i, x in enumerate(nums):
        need = target - x
        if need in index_of:             # check BEFORE storing x (no self-pairing)
            return [index_of[need], i]
        index_of[x] = i
    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([3, 5], 6) == []
```

**Trace** — `[2, 7, 11, 15]`, target 9: i=0, need 7, not seen, store {2:0};
i=1, need 2, **seen at 0** → `[0, 1]`.

### 9.8 First non-repeating character (count, then scan)

```python
def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):           # second pass keeps the original order
        if counts[ch] == 1:
            return i
    return -1


assert first_unique("leetcode") == 0 and first_unique("loveleetcode") == 2
assert first_unique("aabb") == -1
```

### 9.9 Anagrams: check and group

```python
def is_anagram(a, b):
    if len(a) != len(b):
        return False
    counts = {}
    for ch in a:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in b:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1
    return True


def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))         # every anagram has the same sorted form
        groups.setdefault(key, []).append(w)
    return list(groups.values())


assert is_anagram("listen", "silent") and not is_anagram("rat", "car")
assert sorted(map(sorted, group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))) == \
    [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
```

The key must be hashable: `sorted(w)` gives a list (unhashable), so turn it
into a string or tuple.

### 9.10 Intersection of two arrays

```python
def intersection(a, b):
    return list(set(a) & set(b))          # unique common values


def intersection_with_counts(a, b):
    """Keep duplicates as many times as they appear in both."""
    counts = {}
    for x in a:
        counts[x] = counts.get(x, 0) + 1
    out = []
    for x in b:
        if counts.get(x, 0) > 0:
            out.append(x)
            counts[x] -= 1
    return out


assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
assert intersection_with_counts([1, 2, 2, 1], [2, 2]) == [2, 2]
```

### 9.11 Longest substring without repeating characters (sliding window + map)

Keep a window `[left, right]` with no repeats; the map remembers where each
character was last seen, so `left` can jump straight past the duplicate.

```python
def longest_unique_substring(s):
    last_seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:   # repeat inside the window
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


assert longest_unique_substring("abcabcbb") == 3     # "abc"
assert longest_unique_substring("bbbbb") == 1
assert longest_unique_substring("pwwkew") == 3       # "wke"
assert longest_unique_substring("") == 0
```

### 9.12 Subarray sum equals k (prefix sums + map)

```python
def count_subarrays_with_sum(nums, k):
    seen = {0: 1}             # prefix sum 0 has "happened" once: before index 0
    prefix = count = 0
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)   # earlier prefixes that leave exactly k
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


assert count_subarrays_with_sum([1, 1, 1], 2) == 2
assert count_subarrays_with_sum([1, -1, 1, -1], 0) == 4
```

sum(i..j) = prefix[j] − prefix[i−1]. We want that to equal k, i.e.
prefix[i−1] = prefix[j] − k: "how many times have I already seen `prefix − k`?"

### 9.13 LRU cache (hash map + doubly linked list)

The map finds a node in O(1); the list keeps nodes in recency order so
"move to most recent" and "evict least recent" are O(1) too.

```python
class _Node:
    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}                          # key -> node
        self.head, self.tail = _Node(), _Node()   # sentinels: head.next = LEAST recent
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_to_end(self, node):               # end = most recent
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)                     # it was just used:
        self._add_to_end(node)                 # move to the most-recent end
        return node.value

    def put(self, key, value):
        if key in self.map:
            self._remove(self.map[key])
        elif len(self.map) == self.capacity:
            lru = self.head.next               # least recently used
            self._remove(lru)
            del self.map[lru.key]              # the node stores its key for this
        node = _Node(key, value)
        self.map[key] = node
        self._add_to_end(node)


cache = LRUCache(2)
cache.put(1, 1); cache.put(2, 2)
assert cache.get(1) == 1          # order (LRU -> MRU): 2, 1
cache.put(3, 3)                   # evicts 2
assert cache.get(2) == -1
cache.put(4, 4)                   # evicts 1
assert cache.get(1) == -1 and cache.get(3) == 3 and cache.get(4) == 4
```

### 9.14 Complexity summary

| Algorithm | Time | Space | Brute force it replaces |
|---|---|---|---|
| Contains duplicate | O(n) | O(n) | O(n²) all pairs |
| Two sum | O(n) | O(n) | O(n²) all pairs |
| First unique char | O(n) | O(k) | O(n²) `count` per char |
| Group anagrams | O(n·k log k) | O(n·k) | O(n²·k) compare every pair |
| Longest unique substring | O(n) | O(k) | O(n³) check every substring |
| Subarray sum = k | O(n) | O(n) | O(n²) every subarray |
| LRU get/put | O(1) | O(capacity) | O(n) with a list |

## 10. Tasks

| #  | Task                                  | Difficulty | LeetCode | File |
|----|---------------------------------------|------------|----------|------|
| 01 | Build a Hash Map (chaining + resize)  | Core       | (706)    | `tasks/t01_core_hash_map.py` |
| 02 | Two Sum                               | Easy       | 1        | `tasks/t02_easy_two_sum.py` |
| 03 | Valid Anagram                         | Easy       | 242      | `tasks/t03_easy_valid_anagram.py` |
| 04 | First Unique Character                | Easy       | 387      | `tasks/t04_easy_first_unique_char.py` |
| 05 | Group Anagrams                        | Medium     | 49       | `tasks/t05_medium_group_anagrams.py` |
| 06 | Top K Frequent Elements               | Medium     | 347      | `tasks/t06_medium_top_k_frequent.py` |
| 07 | Longest Consecutive Sequence          | Medium     | 128      | `tasks/t07_medium_longest_consecutive.py` |
| 08 | Subarray Sum Equals K                 | Medium     | 560      | `tasks/t08_medium_subarray_sum_k.py` |
| 09 | LRU Cache                             | Hard       | 146      | `tasks/t09_hard_lru_cache.py` |
| 10 | Minimum Window Substring              | Hard       | 76       | `tasks/t10_hard_min_window_substring.py` |

t09 (LRU Cache) combines this module with Module 2: it uses `DListNode` from
`m02_linked_lists/framework.py`.

```bash
pytest m04_hashmaps
pytest m04_hashmaps/tests/test_t01_core_hash_map.py -x
python progress.py m04
```
