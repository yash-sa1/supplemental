"""
Task 01 · Easy · Big O Quiz

For each snippet below, work out its complexity and write it into ANSWERS.
Unless the question says SPACE, it's asking for TIME complexity, worst case,
in terms of n = len(arr) (and m = len(b) where there's a second input).

Answer format: write normal Big O, e.g.
    "O(1)"  "O(log n)"  "O(n)"  "O(n log n)"  "O(n^2)"  "O(n^3)"  "O(2^n)"  "O(n + m)"  "O(n * m)"
Spacing/case don't matter; "n**2", "n²" and "log(n)" are also accepted.

The tests store hashed answers, so you can't peek at them in the test file.
Reason it out, then run the tests.
"""

ANSWERS = {
    "q01": "",
    "q02": "",
    "q03": "",
    "q04": "",
    "q05": "",
    "q06": "",
    "q07": "",
    "q08": "",
    "q09": "",
    "q10": "",
    "q11": "",
    "q12": "",
    "q13": "",
    "q14": "",  # SPACE complexity
    "q15": "",  # SPACE complexity
    "q16": "",
    "q17": "",
}


def q01(arr):
    total = 0
    for x in arr:
        total += x
    return total


def q02(arr):
    return arr[0] if arr else None


def q03(arr):
    pairs = 0
    for a in arr:
        for b in arr:
            if a + b == 0:
                pairs += 1
    return pairs


def q04(arr):
    n = len(arr)
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps


def q05(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            count += 1
    return count


def q06(arr, b):
    for x in arr:
        print(x)
    for y in b:
        print(y)


def q07(arr, b):
    for x in arr:
        for y in b:
            print(x, y)


def q08(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # inner loop shrinks each time...
            if arr[i] == arr[j]:
                return True
    return False


def q09(arr):
    for x in arr:
        for k in range(5):
            print(x * k)


def q10(n):  # complexity in terms of the number n itself
    if n <= 1:
        return n
    return q10(n - 1) + q10(n - 2)


def q11(arr):
    seen = []
    for x in arr:
        if x not in seen:  # `in` on a list
            seen.append(x)
    return seen


def q12(arr):
    seen = set()
    for x in arr:
        if x not in seen:  # `in` on a set
            seen.add(x)
    return seen


def q13(arr):
    if not arr:
        return 0
    return arr[0] + q13(arr[1:])  # careful: what does arr[1:] cost?


def q14(arr, i=0):  # SPACE complexity (think about the call stack)
    if i == len(arr):
        return 0
    return arr[i] + q14(arr, i + 1)


def q15(arr):  # SPACE complexity
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1
    return arr


def q16(arr):
    ordered = sorted(arr)
    for i in range(1, len(ordered)):
        if ordered[i] == ordered[i - 1]:
            return True
    return False


def q17(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    count += 1
    return count
