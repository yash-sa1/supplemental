"""
Task 10 · Hard · Largest Rectangle in Histogram  (LeetCode #84)

Given bar heights of a histogram where every bar has width 1, return the area
of the largest rectangle that fits entirely inside the histogram.

Example 1:
    Input:  [2, 1, 5, 6, 2, 3]
    Output: 10        (bars 5 and 6: height 5 * width 2)

            #
          # #
          # #
          # #   #
      #   # # # #
      # # # # # #
      2 1 5 6 2 3

Example 2:
    Input:  [2, 4]
    Output: 4

Constraints:
    - 0 <= len(heights) <= 10^5
    - 0 <= heights[i] <= 10^4

Target: O(n) time with a monotonic stack. (Checking every pair of bars is
O(n^2) and times out.)
"""


def largest_rectangle_area(heights: list[int]) -> int:
    raise NotImplementedError
