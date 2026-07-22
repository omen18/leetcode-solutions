"""
Problem: Largest Rectangle in Histogram
LeetCode #: 84
Difficulty: Hard
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Approach:
Use a monotonic increasing stack storing tuples of `(index, height)`.
Iterate through the histogram `heights`:
- For each height, maintain `start_idx = current_index`.
- While stack is non-empty and stack top height > current height:
  - Pop from stack `(pop_idx, pop_h)`.
  - Calculate area `pop_h * (current_index - pop_idx)` and update `max_area`.
  - Update `start_idx = pop_idx` (since current height can extend leftwards to pop_idx).
- Push `(start_idx, current_height)` to stack.
- After processing all heights, pop remaining items from stack and calculate area up to end of array.

Time Complexity: O(N) where N is length of heights array.
Space Complexity: O(N) for stack.
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stores (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))

        return max_area
