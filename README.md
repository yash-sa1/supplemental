# DSA Exam Prep Workbook

A one-stop shop for the exam modules: theory notes, LeetCode/Codewars-style
tasks with starter code, and unit tests that go after the edge cases.

## Modules

Each module's **README** is the study guide: how the structure works, then an
**Implementation walkthroughs** section with complete, runnable code (and
step-by-step traces) for the structure itself and the classic exam questions.

| #  | Study guide | Topic | Walkthroughs include | Tasks |
|----|-------------|-------|----------------------|-------|
| 1  | [m01_big_o/README.md](m01_big_o/README.md) | Big O, linear & binary search | linear search variants, binary search (iterative/recursive), first/last occurrence, lower/upper bound, binary search on the answer, rotated array, recurrences | 9 |
| 2  | [m02_linked_lists/README.md](m02_linked_lists/README.md) | Linked lists | full linked list class, **reverse (iterative + recursive)**, reverse a section, middle, cycle detection, nth from end, merge, merge sort, remove duplicates, palindrome, intersection, doubly linked list | 10 |
| 3  | [m03_stacks_queues/README.md](m03_stacks_queues/README.md) | Stacks & queues | array/linked stack, linked/circular queue, deque, queue from stacks, stack from queue, balanced brackets, postfix eval, infix→postfix, next greater element, min stack | 11 |
| 4  | [m04_hashmaps/README.md](m04_hashmaps/README.md) | Hash maps & sets | hash functions, chaining map with resize, linear probing with tombstones, hash set, frequency counting, two sum, anagrams, sliding window, prefix sums, LRU cache | 10 |
| 5+ | — | coming soon | | |

## How each module works

```
m02_linked_lists/
  README.md        <- read this first: theory, diagrams, patterns, pitfalls
  framework.py     <- given building blocks (e.g. ListNode) — don't edit
  tasks/           <- YOUR code goes here. Each file: problem statement + stub
  tests/           <- pytest tests for each task (edge cases, big inputs, complexity checks)
  solutions/       <- reference solutions. Don't peek until you've passed (or are truly stuck)
```

Every task file starts with a LeetCode-style problem statement (examples,
constraints, target complexity) and a function/class whose body is
`raise NotImplementedError`. Replace that with your solution.

Task files are named `tNN_<difficulty>_<name>.py`:
**core** = build the data structure itself, then **easy → medium → hard**
problems that use it. Do them in order.

## Running the tests

From the project root:

```bash
python progress.py                  # dashboard: every task, pass counts, DONE marks
python progress.py m02              # just one module

pytest m02_linked_lists                                         # a module
pytest m02_linked_lists/tests/test_t03_easy_reverse_list.py     # one task
pytest m02_linked_lists/tests/test_t03_easy_reverse_list.py -x  # stop at the first failure
pytest m02_linked_lists/tests/test_t03_easy_reverse_list.py -k single   # tests with "single" in the name

pytest --solutions m02_linked_lists  # run the tests against the reference solutions instead
```

**In PyCharm:** right-click a test file (or a single `def test_...`) → *Run 'pytest in …'*.
If PyCharm uses unittest instead, set *Settings → Tools → Python Integrated Tools →
Default test runner → pytest*.

### What the tests check

- The examples from the problem statement.
- Edge cases: empty input, one element, two elements, duplicates, negatives,
  target at the ends, not found, all-equal values…
- Error handling for the data structures you build (e.g. `pop()` on an empty
  stack must raise `IndexError`).
- That you didn't mutate input you shouldn't, and (for linked lists) that you
  re-linked the real nodes rather than copying values.
- **Complexity.** Big inputs that only an efficient algorithm finishes within
  the 5 second per-test limit, and `ProbeArray`, which counts how many
  elements your "O(log n)" search actually read.
- Randomised comparisons against a simple brute-force answer (seeded, so a
  failure is reproducible — the message shows the exact input).

A test that hangs is stopped after 5 seconds with a hint (usually an infinite
loop — e.g. a linked list pointer that now forms a cycle).

## Suggested workflow

1. Read the module README.
2. Open a task, read the statement, and work through the examples by hand.
3. Write your solution, then run that task's tests with `-x`.
4. Read the failing test's name and message — it usually says which edge case you missed.
5. Once it's green, compare with `solutions/` for a different angle.
6. Before the exam: re-do the core tasks from a blank stub, timed.
