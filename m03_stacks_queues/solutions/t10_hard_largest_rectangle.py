"""
Task 10 · Hard · Largest Rectangle in Histogram  (SOLUTION)

Keep a stack of bar indices with increasing heights. When a shorter bar
arrives at index i, every taller bar on the stack has found its right
boundary (i). Pop it: its left boundary is the new stack top (the nearest
shorter bar to its left), so its widest rectangle has
    width = i - stack_top - 1      (or i if the stack is now empty).
A sentinel height 0 at the end flushes the stack.
"""


def largest_rectangle_area(heights: list[int]) -> int:
    best = 0
    stack: list[int] = []  # indices, heights strictly increasing
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, height * (i - left - 1))
        stack.append(i)
    return best
