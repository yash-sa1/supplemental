# CLAUDE.md — DSA Exam Prep Workbook

This repo is a self-contained study workbook for a data structures & algorithms
coding exam. Each exam module gets its own folder with theory notes, LeetCode /
Codewars-style tasks (starter stubs), reference solutions, and pytest unit
tests that hammer edge cases.

The user will say things like "build module 5 (trees)". Follow this file
exactly so every module feels identical.

## Syllabus / status

| #  | Folder                 | Topic                                          | Status |
|----|------------------------|------------------------------------------------|--------|
| 1  | `m01_big_o/`           | Big O notation, linear search, binary search   | built  |
| 2  | `m02_linked_lists/`    | Singly/doubly linked lists, pointer techniques | built  |
| 3  | `m03_stacks_queues/`   | Stacks, queues, circular buffers, monotonic    | built  |
| 4  | `m04_hashmaps/`        | Hash maps/sets, hashing, chaining, resizing    | built  |
| 5+ | —                      | Not given yet — ask the user for the topic list | todo  |

When a new module is built, update this table and the table in `README.md`.

## Environment

- Python 3.13 (PyCharm project interpreter), pytest 9. No other deps — don't add any.
- Run everything from the repo root. `pytest.ini` sets `pythonpath = .` and
  `--import-mode=importlib`, so imports look like `from m02_linked_lists.framework import ListNode`.
- `python progress.py` prints a per-task pass/fail dashboard.

## Repo layout

```
CLAUDE.md                 this file
README.md                 how to use the workbook (student-facing)
pytest.ini                pytest config
conftest.py               per-test timeout (catches infinite loops) + --solutions flag
progress.py               dashboard: python progress.py [m02] [--solutions]
common/
  loader.py               load_task(__file__) -> imports the task (or solution) under test
  probes.py               ProbeArray: counts element reads to enforce O(log n) etc.
mXX_topic/
  README.md               theory notes + task table (student-facing)
  framework.py            (optional) given building blocks, e.g. ListNode + helpers
  tasks/                  STUBS the student edits. Every function body: raise NotImplementedError
    __init__.py
    tNN_<difficulty>_<name>.py
  solutions/              reference solutions, same filenames + same public API as tasks/
    __init__.py
    tNN_<difficulty>_<name>.py
  tests/
    test_tNN_<difficulty>_<name>.py
```

## Naming conventions

- Module folders: `mNN_<topic>` (two-digit number, snake_case topic).
- Task files: `tNN_<difficulty>_<name>.py`, numbered in order of difficulty so
  they sort nicely. `<difficulty>` is one of `core`, `easy`, `medium`, `hard`.
  - `core`  = "build the data structure itself" (e.g. SinglyLinkedList, Stack, HashMap).
  - `easy` / `medium` / `hard` = LeetCode-style problems using the structure.
- Test file = `test_` + task filename. `load_task(__file__)` relies on this:
  it strips `test_` and imports `<module>.tasks.<name>` (or `.solutions.` when
  `--solutions` / `DSA_SOLUTIONS=1` is set). Never import tasks directly in tests.

## Module recipe (do all of these for every new module)

1. **Task mix** — aim for 8–10 tasks: 1–2 `core`, 3 `easy`, 3–4 `medium`, 2 `hard`.
   Prefer well-known LeetCode problems (cite the number in the docstring) that
   are exam-typical for the topic.
2. **Task stub** (`tasks/…`): module docstring in this format:
   ```
   """
   Task NN · <Difficulty> · <Title>  (LeetCode #123)   <- omit LC ref if not from LC

   <Problem statement, LeetCode style.>

   Example 1:
       Input:  ...
       Output: ...

   Constraints:
       - ...

   Target: O(?) time, O(?) extra space.
   """
   ```
   Then the function/class signatures with type hints, a one-line docstring per
   method where the contract isn't obvious (return values, what to raise), and
   `raise NotImplementedError` bodies. NO hints or partial solutions in stubs.
   Stubs must import cleanly (tests should FAIL, not ERROR at collection).
3. **Solution** (`solutions/…`): clean, idiomatic, commented where the trick
   is non-obvious. Identical public API to the stub.
4. **Tests** (`tests/…`): pytest, plain functions, descriptive names
   (`test_single_node`, `test_target_smaller_than_all`). Cover:
   - the docstring examples,
   - edge cases: empty input, single element, two elements, duplicates,
     negatives/zero, all-same values, target at first/last position, not found,
     very large input,
   - error contracts (`pytest.raises(IndexError)` etc.) for core structures,
   - mutation checks (does it modify input when it shouldn't / is it in-place when it should be),
   - complexity checks where measurable: `ProbeArray` read-count bounds for
     log-time searches, or a large input that only an efficient solution
     finishes within the 5s per-test timeout (keep brute-force-kills realistic:
     the efficient solution should run in well under 1s),
   - a randomized test against a brute-force oracle where it makes sense
     (seeded `random.Random(…)` so failures are reproducible).
   Assertion messages should help the student debug (show input/expected).
   Test the contract, not the implementation (don't depend on private attrs,
   except documented ones like `capacity` on the HashMap).
5. **README.md** for the module:
   - Concept explanation from zero (what, why, mental model, ASCII diagrams),
   - operations + Big O table,
   - common techniques/patterns for the topic (e.g. fast/slow pointers, dummy head),
   - pitfalls & exam tips,
   - **`## N. Implementation walkthroughs (the stuff exams ask you to write)`** —
     the student explicitly wants this. FULL working code for the data structure
     itself (complete class) and every commonly asked classic for the topic
     (e.g. m02: reverse iterative + recursive, middle, Floyd cycle, merge, palindrome,
     intersection…), each with comments, a step-by-step trace table/diagram for
     the key ones, `assert` examples, and a closing complexity summary table.
     Overlap with task solutions is fine. Every ```python block after that
     heading must be self-contained when run top-to-bottom in one namespace
     (define nodes inline; don't import framework), and use ```text for
     pseudo-code. Verify by extracting and exec'ing them (see step 6),
   - task table: `| # | Task | Difficulty | LeetCode | File |` plus run commands.
6. **Verify before finishing** (mandatory):
   - `pytest mNN_* --solutions -q` → 100% pass, and every test well under 1s
     (`--durations=5`).
   - `pytest mNN_* -q` → every test fails with NotImplementedError, zero
     collection errors. (Tests that would pass on an empty stub, like "doesn't
     use deque", must call the code first so they fail too.)
   - Mutation check: copy the repo to the scratchpad, drop in a few typical
     wrong answers (off-by-one, stale tail pointer, O(n²) brute force,
     `list.pop(0)` queue…) and confirm the tests catch each. Timing-based
     tests need the slow version to take >>5s (aim for 10x), not just "a bit over".
   - `python progress.py mNN` renders.
   - README walkthrough code runs: extract every ```python block after the
     "Implementation walkthroughs" heading and exec them in order in one
     namespace; all asserts pass.
7. Add the module folder to `testpaths` in `pytest.ini`.
8. Update the syllabus tables here and in the root `README.md`.

## Shared helpers

- `common/loader.py::load_task(__file__)` — returns the imported task module.
- `common/probes.py::ProbeArray(values)` — read-only sequence; `.reads` counts
  `arr[i]` accesses, slicing raises `TypeError` (slicing copies = O(n)). Use for
  anything claiming sub-linear time on arrays.
- `conftest.py` — every test has a 5s timeout (SIGALRM, macOS/Linux) so an
  infinite loop (e.g. a lost `next` pointer creating a cycle) fails fast with a hint.
- `m02_linked_lists/framework.py` — `ListNode`, `DListNode`, `from_list`,
  `to_list` (cycle-safe), `nodes_of`. Later modules may import from it
  (e.g. m04 LRU cache uses `DListNode`).

## Working with the student

- The student edits `tasks/`. Never overwrite a task file they've started on
  without asking; check if it still only contains `raise NotImplementedError`.
- If they ask for help on a task: give a hint first (the pattern / the invariant /
  which edge case is failing and why), then escalate to pseudocode, and only
  show full code if they explicitly ask. Point them to `solutions/` if they
  want to compare after solving.
- When they ask to explain a failing test, run that single test and explain
  what input broke and why.
