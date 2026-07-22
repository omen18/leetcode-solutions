"""
Problem: Max Area of Island
LeetCode #: 695
Difficulty: Medium
Link: https://leetcode.com/problems/max-area-of-island/

Approach: Traverse grid cells. Perform DFS on every unvisited land cell ('1') to compute area by recursively visiting adjacent land cells and zeroing out visited ones.
Time Complexity: O(M * N) where M and N are grid dimensions.
Space Complexity: O(M * N) for the recursion stack.
"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
