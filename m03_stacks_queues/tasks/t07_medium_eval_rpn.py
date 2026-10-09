"""
Task 07 · Medium · Evaluate Reverse Polish Notation  (LeetCode #150)

In Reverse Polish (postfix) notation the operator comes AFTER its operands:
    "3 4 +"        means 3 + 4
    "2 1 + 3 *"    means (2 + 1) * 3

Given the tokens of an RPN expression, return its integer value.

    - Operators: "+", "-", "*", "/"
    - "/" is integer division that TRUNCATES TOWARD ZERO (like C/Java):
      7 / 2 = 3,  -7 / 2 = -3   (careful: Python's // gives -4 here!)
    - Operands are integers, possibly negative, e.g. "-11".
    - If the expression is malformed (an operator without two operands, or
      leftover operands at the end, or no tokens), raise ValueError.
    - Division by zero may raise ZeroDivisionError.

Example 1:
    Input:  ["2", "1", "+", "3", "*"]
    Output: 9

Example 2:
    Input:  ["4", "13", "5", "/", "+"]
    Output: 6              (4 + 13 / 5 = 4 + 2)

Example 3:
    Input:  ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    Output: 22

Constraints:
    - 0 <= len(tokens) <= 10^4

Target: O(n) time, O(n) space.
"""


def eval_rpn(tokens: list[str]) -> int:
    raise NotImplementedError
