"""
Problem: Maximal Rectangle
LeetCode #: 85
Difficulty: Hard
Link: https://leetcode.com/problems/maximal-rectangle/

Approach:
Reduce problem to LeetCode 84 (Largest Rectangle in Histogram).
Maintain a 1D array `heights` representing histogram column heights up to current matrix row.
For each row in `matrix`:
- If cell is '1', increment `heights[col]` by 1.
- If cell is '0', reset `heights[col]` to 0.
- Compute maximum rectangle area for updated `heights` using monotonic stack algorithm.
Track maximum area across all rows.

Time Complexity: O(R * C) where R is rows, C is columns.
Space Complexity: O(C) to store heights array and monotonic stack.
"""

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_a = 0
            n = len(heights)
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    idx, height = stack.pop()
                    max_a = max(max_a, height * (i - idx))
                    start = idx
                stack.append((start, h))
            for idx, height in stack:
                max_a = max(max_a, height * (n - idx))
            return max_a

        for row in matrix:
            for c in range(cols):
                if row[c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
