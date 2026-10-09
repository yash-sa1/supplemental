# Module 3 — Stacks & Queues

Both are **restricted lists**: you can only add/remove at specific ends. That
restriction is the point — it makes every operation O(1) and matches a lot
of real problems.

## 1. Stack — LIFO (Last In, First Out)

Like a stack of plates: you add to the top and take from the top.

```
push(1) push(2) push(3)        pop() -> 3        peek() -> 2
                  │ 3 │  ◀ top
          │ 2 │   │ 2 │          │ 2 │  ◀ top
  │ 1 │   │ 1 │   │ 1 │          │ 1 │
  └───┘   └───┘   └───┘          └───┘
```

| Operation   | Meaning                         | Cost |
|-------------|---------------------------------|------|
| `push(x)`   | put x on top                    | O(1) |
| `pop()`     | remove and return the top       | O(1) |
| `peek()`/`top()` | look at the top without removing | O(1) |
| `is_empty()`, `len` |                         | O(1) |

**In Python** a list is a perfect stack if you use the **end** as the top:
`append` = push, `pop()` = pop, `[-1]` = peek. (Using the front, `insert(0, x)`
/ `pop(0)`, would be O(n).)

**Where stacks show up**: undo/redo, browser back button, matching brackets,
evaluating expressions, the function **call stack** (recursion!), depth-first
search, "most recent unmatched thing" problems.

## 2. Queue — FIFO (First In, First Out)

Like a line at a shop: join at the back, leave from the front.

```
enqueue →  back [ 4 | 3 | 2 | 1 ] front  → dequeue (returns 1)
```

| Operation     | Meaning                           | Cost |
|---------------|-----------------------------------|------|
| `enqueue(x)`  | add x at the back                 | O(1) |
| `dequeue()`   | remove and return the front       | O(1) |
| `peek()`      | look at the front                 | O(1) |

**Where queues show up**: scheduling (print jobs, CPU tasks), buffering
(keyboard input, network packets), breadth-first search, "process in arrival order".

### Why a Python list is a bad queue
`list.pop(0)` removes the first element and **shifts every other element
left** — O(n). Do it n times → O(n²). Ways to get O(1) at both ends:

1. **Linked list with head + tail pointers** — dequeue at head, enqueue at tail (t02).
2. **Circular buffer (ring buffer)** — fixed-size array + a `head` index that wraps around (t09).
3. **Two stacks** — amortised O(1) (t04).
4. In real code: **`collections.deque`** — O(1) `append`, `appendleft`, `pop`, `popleft`.

```python
from collections import deque
q = deque()
q.append(1); q.append(2)   # enqueue
q.popleft()                # dequeue -> 1
q[0]                       # peek front
```

(`queue.Queue` is a thread-safe queue for concurrent programs — not what you want for algorithms.)

## 3. Deque — double-ended queue

Add/remove at both ends in O(1). A stack and a queue are both special cases.
`collections.deque` is implemented as a doubly linked list of blocks.

## 4. Implementation notes

### Circular buffer (ring buffer)
```
capacity 5, head = 3, count = 4          queue order (front -> back): A B C D

index:   0     1     2     3     4
       [ C  |  D  |  _  |  A  |  B ]
                ▲           ▲
              back        front (head)

enqueue(E) goes to (3 + 4) % 5 = 2 -> the buffer is now full
```
Logical position `i` lives at physical index `(head + i) % capacity`.
- front is at `head`
- back is at `(head + count - 1) % capacity`
- next free slot is `(head + count) % capacity`
- dequeue: `head = (head + 1) % capacity`

Keep a `count` (or waste one slot) — otherwise `head == tail` is ambiguous:
is the buffer empty or full?

### Queue from two stacks
An **in** stack takes pushes. An **out** stack serves pops. When `out` is
empty, pour everything from `in` into `out` — that reverses the order, so
the oldest element ends up on top. Each element moves at most once, so n
operations cost O(n) total → **amortised O(1)**. (Pouring on *every* call is O(n) each.)

### Min stack
To get the minimum in O(1), store alongside each element "the minimum of
everything at or below me". Popping then restores the previous minimum for free.

## 5. Patterns

### Matching / nesting → stack
Brackets, HTML tags, nested function calls: push openers, and a closer must
match the **most recent** unmatched opener (the top).

### Expression evaluation → stack
**Postfix** (Reverse Polish) notation `3 4 + 2 *` needs no brackets: push
numbers; an operator pops two, computes, pushes the result. The first value
popped is the **right** operand. Infix `(3 + 4) * 2` can be converted to
postfix with the shunting-yard algorithm (two stacks).

### Monotonic stack → "next greater / smaller element"
Keep a stack whose values are always increasing (or decreasing). When a new
element breaks the order, pop until it doesn't — each popped element has just
found its "next greater/smaller" element: the new one.

```text
for i, x in enumerate(values):
    while stack and values[stack[-1]] < x:   # x is the next greater for the top
        j = stack.pop()
        answer[j] = ...                     # something involving i and j
    stack.append(i)
```
Every index is pushed and popped **once** → O(n) even though there's a
nested loop. Store **indices**, not values — you usually need distances/widths.
Used in: daily temperatures (t08), largest rectangle in histogram (t10),
stock span, trapping rain water.

### Monotonic deque → sliding window max/min
Same idea but you also drop elements off the **front** when they leave the
window (t11).

### BFS uses a queue, DFS uses a stack
You'll see this again with trees and graphs: breadth-first search explores
level by level using a queue; depth-first search goes deep using a stack
(explicit, or the call stack via recursion).

## 6. Pitfalls

- Pop/peek on an **empty** stack/queue: check first, raise `IndexError`
  (the tests expect this for the core structures).
- Operand order in RPN: `a - b` where `b` is popped **first**.
- Integer division: Python's `//` floors (`-7 // 2 == -4`); many problems
  (LeetCode 150, C, Java) want truncation toward zero (`-3`).
- Linked queue: when the last element is dequeued, reset the **tail** to `None` too.
- Storing values instead of indices in monotonic stacks when you need widths/distances.
- Shared state: `def __init__(self, items=[])` shares one list across all
  instances. Create the list inside `__init__`.

## 7. Implementation walkthroughs (the stuff exams ask you to write)

Every code block below runs as-is, top to bottom (the `assert` lines are examples).

### 7.1 Stack on a Python list

```python
class ArrayStack:
    def __init__(self):
        self._items = []              # the END of the list is the top

    def push(self, val):              # O(1) amortised
        self._items.append(val)

    def pop(self):                    # O(1)
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):                   # O(1)
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


s = ArrayStack()
for v in (1, 2, 3):
    s.push(v)
assert s.pop() == 3 and s.peek() == 2 and len(s) == 2
```

### 7.2 Stack on linked nodes

Push and pop both happen at the **head** — the one place a singly linked list is O(1).

```python
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, val):              # new node points at the old top
        self._top = Node(val, self._top)
        self._size += 1

    def pop(self):
        if self._top is None:
            raise IndexError("pop from empty stack")
        val = self._top.val
        self._top = self._top.next
        self._size -= 1
        return val

    def peek(self):
        if self._top is None:
            raise IndexError("peek at empty stack")
        return self._top.val

    def is_empty(self):
        return self._top is None

    def __len__(self):
        return self._size


ls = LinkedStack()
ls.push("a"); ls.push("b")
assert ls.pop() == "b" and ls.peek() == "a" and len(ls) == 1
```

Array vs linked stack: both O(1). The array version is faster in practice
(memory is contiguous); the linked one never needs to resize.

### 7.3 Queue on linked nodes (head + tail)

Enqueue at the tail, dequeue at the head — both O(1).

```python
class LinkedQueue:
    def __init__(self):
        self._head = None             # front: dequeue here
        self._tail = None             # back: enqueue here
        self._size = 0

    def enqueue(self, val):
        node = Node(val)
        if self._tail is None:        # empty queue
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        val = self._head.val
        self._head = self._head.next
        if self._head is None:        # queue became empty: reset tail too!
            self._tail = None
        self._size -= 1
        return val

    def peek(self):
        if self._head is None:
            raise IndexError("peek at empty queue")
        return self._head.val

    def is_empty(self):
        return self._head is None

    def __len__(self):
        return self._size


q = LinkedQueue()
q.enqueue(1); q.enqueue(2)
assert q.dequeue() == 1 and q.dequeue() == 2 and q.is_empty()
q.enqueue(3)                           # works again after being emptied
assert q.peek() == 3
```

### 7.4 Circular queue (ring buffer)

Fixed-size array; indices wrap around with `% capacity`.

```python
class CircularQueue:
    def __init__(self, capacity):
        self._buf = [None] * capacity
        self._cap = capacity
        self._head = 0                # index of the front element
        self._count = 0               # how many elements are stored

    def enqueue(self, val):
        if self._count == self._cap:
            return False              # full
        back = (self._head + self._count) % self._cap
        self._buf[back] = val
        self._count += 1
        return True

    def dequeue(self):
        if self._count == 0:
            raise IndexError("dequeue from empty queue")
        val = self._buf[self._head]
        self._buf[self._head] = None
        self._head = (self._head + 1) % self._cap   # front moves forward, wrapping
        self._count -= 1
        return val

    def front(self):
        if self._count == 0:
            raise IndexError("empty")
        return self._buf[self._head]

    def rear(self):
        if self._count == 0:
            raise IndexError("empty")
        return self._buf[(self._head + self._count - 1) % self._cap]

    def is_full(self):
        return self._count == self._cap


cq = CircularQueue(3)
assert cq.enqueue(1) and cq.enqueue(2) and cq.enqueue(3)
assert not cq.enqueue(4)               # full
assert cq.dequeue() == 1
assert cq.enqueue(4)                   # goes into slot 0 (wrapped around)
assert cq._buf == [4, 2, 3] and cq.front() == 2 and cq.rear() == 4
```

**Trace** (capacity 3):

| operation | buf | head | count |
|---|---|---|---|
| enqueue 1,2,3 | `[1, 2, 3]` | 0 | 3 |
| dequeue → 1 | `[_, 2, 3]` | 1 | 2 |
| enqueue 4 → slot (1+2)%3 = 0 | `[4, 2, 3]` | 1 | 3 |
| dequeue → 2 | `[4, _, 3]` | 2 | 2 |
| dequeue → 3 | `[4, _, _]` | 0 (wrapped) | 1 |

### 7.5 Using Python's deque (what you'd write in real code)

```python
from collections import deque

dq = deque()
dq.append(1); dq.append(2)             # as a queue: add to the right...
assert dq.popleft() == 1               # ...remove from the left, O(1)
dq.appendleft(0)                       # as a deque: both ends are O(1)
assert list(dq) == [0, 2] and dq.pop() == 2

window = deque(maxlen=3)               # auto-drops from the left when full
for x in range(5):
    window.append(x)
assert list(window) == [2, 3, 4]
```

### 7.6 Queue from two stacks (amortised O(1))

```python
class QueueFromStacks:
    def __init__(self):
        self._in = []                 # receives pushes
        self._out = []                # serves pops, oldest on top

    def push(self, x):
        self._in.append(x)

    def _move_if_needed(self):
        if not self._out:             # ONLY refill when out is empty
            while self._in:
                self._out.append(self._in.pop())   # reverses the order

    def pop(self):
        self._move_if_needed()
        if not self._out:
            raise IndexError("empty queue")
        return self._out.pop()

    def peek(self):
        self._move_if_needed()
        if not self._out:
            raise IndexError("empty queue")
        return self._out[-1]


qs = QueueFromStacks()
qs.push(1); qs.push(2)
assert qs.pop() == 1
qs.push(3)                             # goes into _in; _out still holds 2
assert [qs.pop(), qs.pop()] == [2, 3]
```

Refilling `out` while it still has items would put newer elements on top of
older ones and break FIFO order.

### 7.7 Stack from a queue

After each push, rotate the queue so the newest element comes to the front.
Push is O(n), pop is O(1).

```python
from collections import deque


class StackFromQueue:
    def __init__(self):
        self._q = deque()

    def push(self, x):
        self._q.append(x)
        for _ in range(len(self._q) - 1):   # move everything older behind x
            self._q.append(self._q.popleft())

    def pop(self):
        if not self._q:
            raise IndexError("empty stack")
        return self._q.popleft()


sq = StackFromQueue()
for v in (1, 2, 3):
    sq.push(v)
assert [sq.pop(), sq.pop(), sq.pop()] == [3, 2, 1]
```

### 7.8 Balanced brackets

```python
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False          # closer with no opener, or the wrong opener
    return not stack                  # leftover openers = unbalanced


assert is_balanced("{[()()]}") and is_balanced("f(a[1]) + {x}")
assert not is_balanced("([)]") and not is_balanced("((") and not is_balanced(")")
```

**Trace** on `"{[()]}"`:

| char | action | stack |
|---|---|---|
| `{` | push | `{` |
| `[` | push | `{ [` |
| `(` | push | `{ [ (` |
| `)` | pop `(` ✓ | `{ [` |
| `]` | pop `[` ✓ | `{` |
| `}` | pop `{` ✓ | empty → balanced |

### 7.9 Reverse a string / list with a stack

```python
def reverse_with_stack(text):
    stack = list(text)                # push every char
    out = []
    while stack:
        out.append(stack.pop())       # pop comes out in reverse order
    return "".join(out)


assert reverse_with_stack("hello") == "olleh"
```

### 7.10 Evaluate a postfix (Reverse Polish) expression

```python
def eval_postfix(tokens):
    stack = []
    for tok in tokens:
        if tok in ("+", "-", "*", "/"):
            b = stack.pop()           # RIGHT operand comes off first
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))   # truncate toward zero (fine for small ints)
        else:
            stack.append(int(tok))
    return stack.pop()


assert eval_postfix("3 4 + 2 *".split()) == 14          # (3 + 4) * 2
assert eval_postfix("5 1 2 + 4 * + 3 -".split()) == 14  # 5 + (1 + 2) * 4 - 3
assert eval_postfix("7 -2 /".split()) == -3
```

**Trace** on `3 4 + 2 *`: push 3 → `[3]`, push 4 → `[3, 4]`, `+` pops 4 and 3
→ push 7 → `[7]`, push 2 → `[7, 2]`, `*` pops 2 and 7 → push 14 → answer 14.

### 7.11 Infix → postfix (shunting-yard algorithm)

Convert `3 + 4 * 2` into `3 4 2 * +` using an operator stack.

Rules:
- number → output
- `(` → push
- `)` → pop operators to output until `(`, then discard the `(`
- operator → first pop operators with **higher or equal** precedence (left
  associative) to output, then push it
- at the end, pop everything left

```python
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2}


def infix_to_postfix(tokens):
    output, ops = [], []
    for tok in tokens:
        if tok in PRECEDENCE:
            while ops and ops[-1] != "(" and PRECEDENCE[ops[-1]] >= PRECEDENCE[tok]:
                output.append(ops.pop())
            ops.append(tok)
        elif tok == "(":
            ops.append(tok)
        elif tok == ")":
            while ops[-1] != "(":
                output.append(ops.pop())
            ops.pop()                 # discard the "("
        else:
            output.append(tok)        # a number
    while ops:
        output.append(ops.pop())
    return output


assert infix_to_postfix("3 + 4 * 2".split()) == "3 4 2 * +".split()
assert infix_to_postfix("( 3 + 4 ) * 2".split()) == "3 4 + 2 *".split()
assert infix_to_postfix("8 - 3 - 2".split()) == "8 3 - 2 -".split()   # left-assoc
assert eval_postfix(infix_to_postfix("( 1 + 2 ) * ( 3 + 4 ) - 5".split())) == 16
```

**Trace** on `3 + 4 * 2`:

| token | output | ops stack | why |
|---|---|---|---|
| 3 | `3` | | number |
| + | `3` | `+` | stack empty, push |
| 4 | `3 4` | `+` | number |
| * | `3 4` | `+ *` | `*` beats `+`, nothing popped |
| 2 | `3 4 2` | `+ *` | number |
| end | `3 4 2 * +` | | pop the rest |

### 7.12 Next greater element (monotonic stack)

For each element, the first bigger element to its right (or -1).

```python
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []                        # indices still waiting; values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x   # x is the answer for everything smaller on top
        stack.append(i)
    return result


assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
assert next_greater([5, 4, 3]) == [-1, -1, -1]
```

**Trace** on `[2, 1, 2, 4, 3]` (stack shows values):

| i | x | pops (and sets) | stack after |
|---|---|---|---|
| 0 | 2 | — | `2` |
| 1 | 1 | — | `2 1` |
| 2 | 2 | 1 → result[1] = 2 | `2 2` |
| 3 | 4 | 2 → result[2] = 4, 2 → result[0] = 4 | `4` |
| 4 | 3 | — | `4 3` (both stay -1) |

Variations: next **smaller** (flip `<` to `>`), previous greater (loop
right-to-left), distances instead of values (`i - j`, as in Daily Temperatures).

### 7.13 Min stack

```python
class MinStack:
    def __init__(self):
        self._items = []              # (value, min of everything up to here)

    def push(self, val):
        current_min = val if not self._items else min(val, self._items[-1][1])
        self._items.append((val, current_min))

    def pop(self):
        return self._items.pop()[0]

    def top(self):
        return self._items[-1][0]

    def get_min(self):
        return self._items[-1][1]     # O(1): no scanning


ms = MinStack()
for v in (5, 3, 7, 3):
    ms.push(v)
assert ms.get_min() == 3
ms.pop(); ms.pop()                    # remove 3 and 7
assert ms.get_min() == 3
ms.pop()                              # remove the other 3
assert ms.get_min() == 5
```

### 7.14 Complexity summary

| Structure / algorithm | Operations | Time |
|---|---|---|
| ArrayStack / LinkedStack | push, pop, peek | O(1) |
| LinkedQueue / CircularQueue / deque | enqueue, dequeue, peek | O(1) |
| Queue as a Python list | `pop(0)` | **O(n)** |
| Queue from two stacks | push, pop | O(1) amortised |
| Stack from a queue | push / pop | O(n) / O(1) |
| Balanced brackets, postfix eval, shunting-yard | whole input | O(n) time, O(n) space |
| Monotonic stack (next greater) | whole input | O(n) — each index pushed and popped once |
| Min stack | all | O(1) |

## 8. Tasks

| #  | Task                                 | Difficulty | LeetCode | File |
|----|--------------------------------------|------------|----------|------|
| 01 | Build a Stack                        | Core       | —        | `tasks/t01_core_stack.py` |
| 02 | Build a Queue (linked nodes)         | Core       | —        | `tasks/t02_core_queue.py` |
| 03 | Valid Parentheses                    | Easy       | 20       | `tasks/t03_easy_valid_parentheses.py` |
| 04 | Implement Queue using Stacks         | Easy       | 232      | `tasks/t04_easy_queue_via_stacks.py` |
| 05 | Backspace String Compare             | Easy       | 844      | `tasks/t05_easy_backspace_compare.py` |
| 06 | Min Stack                            | Medium     | 155      | `tasks/t06_medium_min_stack.py` |
| 07 | Evaluate Reverse Polish Notation     | Medium     | 150      | `tasks/t07_medium_eval_rpn.py` |
| 08 | Daily Temperatures                   | Medium     | 739      | `tasks/t08_medium_daily_temperatures.py` |
| 09 | Design Circular Queue                | Medium     | 622      | `tasks/t09_medium_circular_queue.py` |
| 10 | Largest Rectangle in Histogram       | Hard       | 84       | `tasks/t10_hard_largest_rectangle.py` |
| 11 | Sliding Window Maximum               | Hard       | 239      | `tasks/t11_hard_sliding_window_max.py` |

```bash
pytest m03_stacks_queues
pytest m03_stacks_queues/tests/test_t06_medium_min_stack.py -x
python progress.py m03
```

The "constant time" tests use inputs of 10⁵–10⁶ operations: an O(n) operation
hidden inside (like `list.pop(0)` or scanning for the minimum) blows the 5s timeout.
