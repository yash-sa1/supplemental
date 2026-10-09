# Module 2 — Linked Lists

## 1. What is a linked list?

An array stores elements **next to each other** in memory, so `arr[i]` is one
jump. A linked list stores each element in its own **node** somewhere in
memory, and each node holds a **pointer** (reference) to the next one.

```
Array:        [ 7 | 3 | 9 | 4 ]          one block, index = offset

Linked list:  head
               │
               ▼
             ┌───┬───┐   ┌───┬───┐   ┌───┬───┐   ┌───┬──────┐
             │ 7 │ ●─┼──▶│ 3 │ ●─┼──▶│ 9 │ ●─┼──▶│ 4 │ None │
             └───┴───┘   └───┴───┘   └───┴───┘   └───┴──────┘
              val next
```

The list itself is just a reference to the **head** node. The last node's
`next` is `None`. To reach element i you must walk i pointers → no O(1) indexing.

**Why bother?** Inserting/removing at a known position is O(1) — just re-point
a couple of references, nothing shifts. Arrays must shift every later element.

### Variants

| Variant | Node fields | Notes |
|---|---|---|
| Singly linked | `val, next` | can only walk forwards |
| Doubly linked | `val, prev, next` | walk both ways; remove a node in O(1) given the node itself |
| Circular | last `next` → head | used for round-robin scheduling, ring buffers |

## 2. Array vs linked list

| Operation                     | Python list (dynamic array) | Singly linked (head only) | Singly + tail pointer | Doubly + tail |
|-------------------------------|-----------------------------|---------------------------|-----------------------|---------------|
| Access by index `i`           | **O(1)**                    | O(i)                      | O(i)                  | O(min(i, n−i)) |
| Insert/remove at front        | O(n)                        | **O(1)**                  | **O(1)**              | **O(1)**      |
| Insert at back                | O(1) amortised              | O(n)                      | **O(1)**              | **O(1)**      |
| Remove at back                | O(1)                        | O(n)                      | O(n) ← need the node *before* tail | **O(1)** |
| Insert/remove after a known node | O(n)                     | **O(1)**                  | **O(1)**              | **O(1)**      |
| Search by value               | O(n)                        | O(n)                      | O(n)                  | O(n)          |
| Memory per element            | 1 reference                 | node + 1 pointer          | same                  | node + 2 pointers |

## 3. The building blocks (given in `framework.py`)

```python
from m02_linked_lists.framework import ListNode, DListNode, from_list, to_list, nodes_of

head = from_list([1, 2, 3])    # 1 -> 2 -> 3 -> None
to_list(head)                  # [1, 2, 3]   (raises ValueError if it finds a cycle)
head                           # prints: ListNode(1) -> ListNode(2) -> ListNode(3) -> None
```

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 4. Core moves (learn these until they're automatic)

**Traverse**
```python
node = head
while node is not None:
    ...                 # use node.val
    node = node.next
```

**Insert at the front** — the new node points at the old head, then becomes the head.
```python
head = ListNode(val, head)
```

**Insert after a node `prev`** — order matters: connect the new node to the
rest of the list *before* re-pointing `prev`, or you lose the rest.
```python
prev.next = ListNode(val, prev.next)
```

**Delete the node after `prev`** — skip over it.
```python
prev.next = prev.next.next
```

To delete a node you need the node **before** it. That's why singly linked
deletions usually walk with a `prev` pointer, and why a doubly linked list
can delete any node in O(1).

## 5. Techniques & patterns

### Dummy (sentinel) head
Put a fake node in front of the real head. Now "insert/delete at the head"
is no longer a special case — every real node has a node before it.
Return `dummy.next` at the end.
```python
dummy = ListNode(0, head)
prev = dummy
...
return dummy.next
```
Doubly linked lists often use **two** sentinels (head and tail) so every real
node always has a real `prev` and `next` and you never check for `None`.

### Tail pointer
Keep a reference to the last node so appending is O(1). **Every** operation
that could remove the last node must update it (the #1 bug in t01).

### Fast & slow pointers (tortoise and hare)
`slow` moves 1 step, `fast` moves 2.
- When `fast` reaches the end, `slow` is at the **middle** (t04).
- If there's a **cycle**, `fast` eventually laps `slow` and they meet (t07).
  To find where the cycle starts, restart one pointer at the head and move both
  1 step at a time: they meet at the cycle entrance (Floyd's algorithm).

### Gap / two pointers n apart
Move `fast` n steps ahead first, then move both together. When `fast` hits the
end, `slow` is n from the end (t06).

### Reversal (three pointers)
Walk the list keeping `prev`, `curr` and a saved `next`, flipping one arrow per step:
```
None ← 1    2 → 3 → None        prev=1, curr=2
None ← 1 ← 2    3 → None        prev=2, curr=3
None ← 1 ← 2 ← 3                prev=3, curr=None  -> prev is the new head
```
Reversing a *section* (t09) is the same loop plus careful reconnection of the
section's boundaries.

### Merge (zipper)
Two sorted lists: repeatedly take the smaller front node and attach it to a
tail pointer that starts at a dummy node (t05). Merging k lists: a min-heap of
the k current fronts (t10).

### Recursion on lists
A list is "a node followed by a (smaller) list", so recursion fits naturally,
but it uses O(n) stack space and Python raises `RecursionError` past ~1000
deep. In exams, the iterative version is usually expected unless asked.

## 6. Pitfalls

- **Losing the rest of the list**: overwrite `node.next` before saving it → everything after is gone.
- **`None` checks**: `node.next.next` crashes if `node.next` is `None`.
  In loops, check `fast is not None and fast.next is not None` (in that order).
- **Accidental cycles**: after reversing, the old head must end with `next = None`.
  (`to_list` in the framework detects cycles and the tests have a 5s timeout.)
- **`is` vs `==`**: comparing nodes → use `is` (same object). Comparing values → `==`.
  Lists with duplicate values expose code that compares `.val` when it should compare nodes.
- **Forgetting to update `head`/`tail`/`size`** when the first or last node changes.
- **Empty list and single node**: always test these two by hand before running the tests.

## 7. Implementation walkthroughs (the stuff exams ask you to write)

Every code block below runs as-is, top to bottom (the `assert` lines are
examples). To try them, paste into a Python console in order.

### 7.1 The node and two helpers

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values):
    """[1, 2, 3] -> 1 -> 2 -> 3 -> None, returns head."""
    head = None
    for v in reversed(values):        # build from the back so each node points at the previous head
        head = ListNode(v, head)
    return head


def to_py(head):
    """1 -> 2 -> 3 -> None  ->  [1, 2, 3]"""
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


assert to_py(build([1, 2, 3])) == [1, 2, 3]
assert build([]) is None
```

### 7.2 A complete singly linked list class

This is the "implement a linked list" exam question. It keeps a `tail`
pointer (O(1) append) and a `size` counter (O(1) `len`).

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.val
            node = node.next

    def __str__(self):
        return " -> ".join(map(str, self)) + " -> None"

    # ---------- adding ----------
    def push_front(self, val):                # O(1)
        self.head = ListNode(val, self.head)
        if self.tail is None:                 # list was empty
            self.tail = self.head
        self.size += 1

    def push_back(self, val):                 # O(1) thanks to tail
        node = ListNode(val)
        if self.tail is None:                 # empty: node is head AND tail
            self.head = self.tail = node
        else:
            self.tail.next = node             # old tail points at new node
            self.tail = node                  # new node becomes the tail
        self.size += 1

    def insert_at(self, index, val):          # O(index)
        if not 0 <= index <= self.size:
            raise IndexError("index out of range")
        if index == 0:
            return self.push_front(val)
        if index == self.size:
            return self.push_back(val)
        prev = self.head
        for _ in range(index - 1):            # stop at the node BEFORE the position
            prev = prev.next
        prev.next = ListNode(val, prev.next)  # new node -> rest, then prev -> new node
        self.size += 1

    # ---------- removing ----------
    def pop_front(self):                      # O(1)
        if self.head is None:
            raise IndexError("pop from empty list")
        val = self.head.val
        self.head = self.head.next
        if self.head is None:                 # removed the last node
            self.tail = None
        self.size -= 1
        return val

    def delete_at(self, index):               # O(index)
        if not 0 <= index < self.size:
            raise IndexError("index out of range")
        if index == 0:
            return self.pop_front()
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        target = prev.next
        prev.next = target.next               # skip over target
        if target is self.tail:               # removed the last node: tail moves back
            self.tail = prev
        self.size -= 1
        return target.val

    def delete_value(self, val):              # O(n): first match only
        prev, node = None, self.head
        while node is not None:
            if node.val == val:
                if prev is None:
                    self.pop_front()
                else:
                    prev.next = node.next
                    if node is self.tail:
                        self.tail = prev
                    self.size -= 1
                return True
            prev, node = node, node.next      # walk with a trailing pointer
        return False

    # ---------- reading ----------
    def get(self, index):                     # O(index)
        if not 0 <= index < self.size:
            raise IndexError("index out of range")
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def search(self, val):                    # O(n)
        for i, v in enumerate(self):
            if v == val:
                return i
        return -1


sll = SinglyLinkedList()
sll.push_back(2); sll.push_back(3); sll.push_front(1)   # 1 -> 2 -> 3
sll.insert_at(1, 9)                                     # 1 -> 9 -> 2 -> 3
assert str(sll) == "1 -> 9 -> 2 -> 3 -> None"
assert sll.delete_at(3) == 3 and sll.tail.val == 2      # tail moved back
sll.push_back(4)
assert list(sll) == [1, 9, 2, 4] and len(sll) == 4
assert sll.delete_value(9) and not sll.delete_value(42)
assert sll.search(4) == 2 and sll.get(0) == 1
```

**Insert-at-position picture** (`insert_at(2, X)` into `A -> B -> C`):
```
walk prev to index 1:   A -> B -> C          prev = B
new node points on:            X -> C
prev points at it:      A -> B -> X -> C
```
Do it in the other order (`prev.next = X` first) and you've lost `C`.

### 7.3 Reverse a linked list — iterative (THE classic)

Three pointers: `prev` (already reversed part), `curr` (node being flipped),
`nxt` (saved so we don't lose the rest).

```python
def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        nxt = curr.next       # 1. save the rest of the list
        curr.next = prev      # 2. flip this node's arrow backwards
        prev = curr           # 3. prev moves up to this node
        curr = nxt            # 4. curr moves on to the saved rest
    return prev               # curr is None; prev is the old tail = new head


assert to_py(reverse(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
assert reverse(None) is None
assert to_py(reverse(build([7]))) == [7]
```

**Trace** on `1 -> 2 -> 3 -> None`:

```
start       prev=None  curr=1        None   1 -> 2 -> 3 -> None
iteration 1 nxt=2, 1.next=None       None <- 1    2 -> 3 -> None     prev=1 curr=2
iteration 2 nxt=3, 2.next=1          None <- 1 <- 2    3 -> None     prev=2 curr=3
iteration 3 nxt=None, 3.next=2       None <- 1 <- 2 <- 3             prev=3 curr=None
return prev (3):                     3 -> 2 -> 1 -> None
```

Time O(n), space O(1). No new nodes: only the `next` arrows change.

### 7.4 Reverse — recursive

"Reverse everything after me, then attach me at the end."

```python
def reverse_recursive(head):
    if head is None or head.next is None:   # 0 or 1 node: already reversed
        return head
    new_head = reverse_recursive(head.next) # reverse the rest: 3 -> 2 (and 2.next is None)
    head.next.next = head                   # the node after me points back at me: 2 -> 1
    head.next = None                        # I'm now the tail (prevents a 1 <-> 2 cycle)
    return new_head                         # the head of the reversed list never changes


assert to_py(reverse_recursive(build([1, 2, 3]))) == [3, 2, 1]
```

```
reverse_recursive(1)                       1 -> 2 -> 3
  reverse_recursive(2)
    reverse_recursive(3) -> returns 3      (base case)
  back in (2): 3.next = 2, 2.next = None   3 -> 2
back in (1): 2.next = 1, 1.next = None     3 -> 2 -> 1
```

Time O(n), space O(n) for the call stack (RecursionError around 1000 nodes in Python).

### 7.5 Reverse only part of a list (positions left..right, 1-indexed)

```python
def reverse_between(head, left, right):
    dummy = ListNode(0, head)
    before = dummy
    for _ in range(left - 1):         # node just before the section
        before = before.next
    # head-insertion: repeatedly move the node after `start` to the front of the section
    start = before.next
    for _ in range(right - left):
        moving = start.next
        start.next = moving.next
        moving.next = before.next
        before.next = moving
    return dummy.next


assert to_py(reverse_between(build([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
assert to_py(reverse_between(build([1, 2]), 1, 2)) == [2, 1]
```

### 7.6 Find the middle — fast & slow pointers

```python
def middle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps
    return slow                   # for even length: the SECOND middle


assert middle(build([1, 2, 3, 4, 5])).val == 3
assert middle(build([1, 2, 3, 4])).val == 3
```

For the FIRST middle of an even list, loop while `fast.next and fast.next.next`.

### 7.7 Detect a cycle and find where it starts (Floyd)

```python
def has_cycle(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:          # `is`: same NODE, not just same value
            return True
    return False


def cycle_start(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:          # they met inside the loop
            finder = head
            while finder is not slow:
                finder = finder.next
                slow = slow.next
            return finder         # both arrive at the loop's entrance together
    return None


looped = build([3, 2, 0, -4])
looped.next.next.next.next = looped.next          # -4 points back to 2
assert has_cycle(looped) and cycle_start(looped) is looped.next
assert not has_cycle(build([1, 2])) and cycle_start(build([1, 2])) is None
```

Why the second phase works: say the tail before the loop has length `a` and
they meet `b` steps into the loop (loop length `L`). Fast walked twice as far
as slow, so `2(a + b) = a + b + kL` → `a = kL − b`. Walking `a` more steps from
the meeting point lands exactly on the loop entrance — the same place a pointer
walking `a` steps from the head reaches.

Easy alternative (O(n) space): remember visited nodes in a `set` and return the
first node you see twice.

### 7.8 Remove the n-th node from the end — one pass

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)     # handles removing the head itself
    fast = slow = dummy
    for _ in range(n):            # open a gap of n nodes
        fast = fast.next
    while fast.next is not None:  # slide the gap to the end
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next    # slow is just BEFORE the target
    return dummy.next


assert to_py(remove_nth_from_end(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert remove_nth_from_end(build([1]), 1) is None
assert to_py(remove_nth_from_end(build([1, 2]), 2)) == [2]
```

### 7.9 Merge two sorted lists

```python
def merge_sorted(a, b):
    dummy = ListNode()
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b   # one list is used up: attach the rest
    return dummy.next


assert to_py(merge_sorted(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
assert to_py(merge_sorted(None, build([0]))) == [0]
```

Merge sort on a linked list = find the middle (7.6), cut, sort both halves, merge.
It's the preferred way to sort linked lists (O(n log n), no random access needed).

```python
def merge_sort_list(head):
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next      # this start gives the FIRST middle
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    second = slow.next
    slow.next = None                  # cut the list in two
    return merge_sorted(merge_sort_list(head), merge_sort_list(second))


assert to_py(merge_sort_list(build([4, 1, 3, 9, 2]))) == [1, 2, 3, 4, 9]
```

### 7.10 Remove duplicates from a SORTED list

```python
def delete_duplicates(head):
    node = head
    while node is not None and node.next is not None:
        if node.next.val == node.val:
            node.next = node.next.next    # skip the duplicate; DON'T advance yet
        else:
            node = node.next
    return head


assert to_py(delete_duplicates(build([1, 1, 2, 3, 3, 3]))) == [1, 2, 3]
```

### 7.11 Palindrome check in O(1) space

Find the middle, reverse the second half, compare the two halves.

```python
def is_palindrome(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    second = reverse(slow)                # reuse 7.3
    first = head
    while second is not None:
        if first.val != second.val:
            return False
        first, second = first.next, second.next
    return True


assert is_palindrome(build([1, 2, 2, 1])) and is_palindrome(build([1, 2, 1]))
assert not is_palindrome(build([1, 2])) and is_palindrome(None)
```

(This modifies the list; in an exam, mention you could reverse the half back afterwards.)

### 7.12 Intersection of two lists

Two lists that merge into a shared tail (`Y` shape). Walk both; when a pointer
hits the end, jump to the OTHER list's head. Both then travel `a + b + c` steps
and meet at the junction (or both become `None`).

```python
def intersection(a_head, b_head):
    a, b = a_head, b_head
    while a is not b:
        a = a.next if a is not None else b_head
        b = b.next if b is not None else a_head
    return a


shared = build([8, 9])
x = build([1, 2]); x.next.next = shared          # 1 -> 2 -> 8 -> 9
y = build([5]);    y.next = shared               # 5 -> 8 -> 9
assert intersection(x, y) is shared
assert intersection(build([1]), build([2])) is None
```

### 7.13 Trick question: delete a node when you're only given that node

No access to the head or the previous node? Copy the next node into this one,
then delete the next node. (Doesn't work for the tail.)

```python
def delete_given_node(node):
    node.val = node.next.val
    node.next = node.next.next


lst = build([4, 5, 1, 9])
delete_given_node(lst.next)                       # "delete 5"
assert to_py(lst) == [4, 1, 9]
```

### 7.14 Doubly linked list with sentinels

Two dummy nodes that never hold data mean every real node has a real `prev`
and `next` — no `None` special cases anywhere.

```
HEAD <-> 10 <-> 20 <-> 30 <-> TAIL
```

```python
class DNode:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = DNode()           # sentinel
        self.tail = DNode()           # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _insert_between(self, val, before, after):   # O(1)
        node = DNode(val)
        node.prev, node.next = before, after
        before.next = node
        after.prev = node
        self.size += 1
        return node

    def _remove(self, node):                          # O(1) given the node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.val

    def push_front(self, val):
        return self._insert_between(val, self.head, self.head.next)

    def push_back(self, val):
        return self._insert_between(val, self.tail.prev, self.tail)

    def pop_front(self):
        if self.size == 0:
            raise IndexError("pop from empty list")
        return self._remove(self.head.next)

    def pop_back(self):
        if self.size == 0:
            raise IndexError("pop from empty list")
        return self._remove(self.tail.prev)

    def forward(self):
        node, out = self.head.next, []
        while node is not self.tail:
            out.append(node.val)
            node = node.next
        return out

    def backward(self):
        node, out = self.tail.prev, []
        while node is not self.head:
            out.append(node.val)
            node = node.prev
        return out


dll = DoublyLinkedList()
dll.push_back(20); dll.push_back(30); dll.push_front(10)
assert dll.forward() == [10, 20, 30] and dll.backward() == [30, 20, 10]
assert dll.pop_back() == 30 and dll.pop_front() == 10
assert dll.forward() == [20] == dll.backward()
```

Inserting between `before` and `after` touches **four** pointers: the new
node's `prev` and `next`, `before.next`, and `after.prev`. Removing touches two.
Checking forward AND backward traversal is the quickest way to catch a missed pointer.

### 7.15 Complexity summary of the classics

| Algorithm | Time | Space | Technique |
|---|---|---|---|
| reverse (iterative) | O(n) | O(1) | prev / curr / next |
| reverse (recursive) | O(n) | O(n) | recursion |
| middle | O(n) | O(1) | fast & slow |
| cycle detect + start | O(n) | O(1) | Floyd |
| n-th from end | O(n) | O(1) | gap of n |
| merge two sorted | O(n + m) | O(1) | dummy + tail |
| merge sort | O(n log n) | O(log n) | middle + merge |
| palindrome | O(n) | O(1) | middle + reverse half |
| intersection | O(n + m) | O(1) | switch heads |

## 8. Tasks

| #  | Task                               | Difficulty | LeetCode  | File |
|----|------------------------------------|------------|-----------|------|
| 01 | Build a Singly Linked List         | Core       | (707)     | `tasks/t01_core_singly_linked_list.py` |
| 02 | Build a Doubly Linked List         | Core       | —         | `tasks/t02_core_doubly_linked_list.py` |
| 03 | Reverse Linked List (iter + recursive) | Easy   | 206       | `tasks/t03_easy_reverse_list.py` |
| 04 | Middle of the Linked List          | Easy       | 876       | `tasks/t04_easy_middle_node.py` |
| 05 | Merge Two Sorted Lists             | Easy       | 21        | `tasks/t05_easy_merge_two_sorted.py` |
| 06 | Remove Nth Node From End           | Medium     | 19        | `tasks/t06_medium_remove_nth_from_end.py` |
| 07 | Linked List Cycle I & II           | Medium     | 141, 142  | `tasks/t07_medium_detect_cycle.py` |
| 08 | Add Two Numbers                    | Medium     | 2         | `tasks/t08_medium_add_two_numbers.py` |
| 09 | Reverse Nodes in k-Group           | Hard       | 25        | `tasks/t09_hard_reverse_k_group.py` |
| 10 | Merge k Sorted Lists               | Hard       | 23        | `tasks/t10_hard_merge_k_sorted.py` |

Do 01 and 02 first — they make every other task feel easier.

```bash
pytest m02_linked_lists
pytest m02_linked_lists/tests/test_t01_core_singly_linked_list.py -x
python progress.py m02
```

The tests don't just check values: many check that you **re-linked the
original nodes** (rather than building new ones or swapping `.val`), that the
input wasn't modified when it shouldn't be, and that `.prev` pointers agree
with `.next` pointers.
