"""
Task 07 · Medium · Evaluate Reverse Polish Notation  (SOLUTION)

Numbers push. An operator pops TWO values — careful with the order: the first
pop is the RIGHT operand — and pushes the result.
"""


def _truncating_div(a: int, b: int) -> int:
    q = abs(a) // abs(b)  # exact integer arithmetic (int(a / b) loses precision on huge ints)
    return q if (a < 0) == (b < 0) else -q


OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": _truncating_div,
}


def eval_rpn(tokens: list[str]) -> int:
    stack: list[int] = []
    for tok in tokens:
        if tok in OPS:
            if len(stack) < 2:
                raise ValueError(f"operator {tok!r} needs two operands")
            b = stack.pop()
            a = stack.pop()
            stack.append(OPS[tok](a, b))
        else:
            stack.append(int(tok))
    if len(stack) != 1:
        raise ValueError("malformed expression")
    return stack[0]
