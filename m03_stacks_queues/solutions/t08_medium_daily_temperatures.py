"""
Task 08 · Medium · Daily Temperatures  (SOLUTION)

Keep a stack of indices of days still WAITING for a warmer day. Their
temperatures are non-increasing from bottom to top (a monotonic stack).
When today is warmer than the top, today is that day's answer: pop and record.
Each index is pushed and popped at most once -> O(n).
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    answer = [0] * len(temperatures)
    waiting: list[int] = []
    for today, temp in enumerate(temperatures):
        while waiting and temperatures[waiting[-1]] < temp:
            day = waiting.pop()
            answer[day] = today - day
        waiting.append(today)
    return answer  # anything still waiting keeps its default 0
