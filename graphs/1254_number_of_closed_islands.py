"""
Problem: Number of Closed Islands
LeetCode #: 1254
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-closed-islands/

Approach: Grid DFS / Boundary Flood Fill.
1. Flood-fill all land cells (0s) connected to the grid boundary since boundary-connected land cannot form a closed island.
2. Iterate through remaining cells and count distinct interior 0 components.

Time Complexity: O(R * C) where R and C are rows and columns of grid.
Space Complexity: O(R * C) for recursion stack.
"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Eliminate boundary land components
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if grid[r][c] == 0:
                        dfs(r, c)

        # Count closed islands in interior
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    count += 1
                    dfs(r, c)

        return count
