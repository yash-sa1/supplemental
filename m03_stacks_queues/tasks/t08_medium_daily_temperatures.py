"""
Task 08 · Medium · Daily Temperatures  (LeetCode #739)

Given a list of daily temperatures, return a list `answer` where answer[i] is
the number of days you have to wait after day i to get a WARMER temperature.
If there's no warmer day ahead, answer[i] = 0.

The nested-loop solution is O(n^2) and will time out. Use a MONOTONIC STACK.

Example 1:
    Input:  [73, 74, 75, 71, 69, 72, 76, 73]
    Output: [1, 1, 4, 2, 1, 1, 0, 0]

Example 2:
    Input:  [30, 40, 50, 60]
    Output: [1, 1, 1, 0]

Example 3:
    Input:  [30, 60, 90]
    Output: [1, 1, 0]

Constraints:
    - 0 <= len(temperatures) <= 10^5
    - 30 <= temperatures[i] <= 100

Target: O(n) time, O(n) space.
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    raise NotImplementedError
