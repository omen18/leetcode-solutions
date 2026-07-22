"""
Problem: Number of Enclaves
LeetCode #: 1020
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-enclaves/

Approach: Flood-fill (DFS) from all boundary land cells ('1') to sink them ('0'). Count remaining land cells which cannot reach boundary.
Time Complexity: O(M * N) where M and N are grid dimensions.
Space Complexity: O(M * N) for recursion stack.
"""

from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        return sum(sum(row) for row in grid)
