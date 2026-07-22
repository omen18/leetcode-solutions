"""
Problem: Daily Temperatures
LeetCode #: 739
Difficulty: Medium
Link: https://leetcode.com/problems/daily-temperatures/

Approach:
Use a monotonic decreasing stack that stores indices of temperatures.
Iterate through the array of temperatures. For each temperature:
- While stack is non-empty and current temperature > temperature at stack top index,
  pop from stack and calculate days waited as `current_index - popped_index`.
- Push current index onto stack.

Time Complexity: O(N) where N is the length of temperatures array.
Space Complexity: O(N) for the stack.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # stores index

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append(i)

        return res
