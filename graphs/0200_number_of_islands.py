"""
Problem: Number of Islands
LeetCode #: 200
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/

Approach: Iterate through the grid. When a cell with '1' is encountered, increment the island counter and launch Depth-First Search (DFS) to sink all connected land cells ('1' -> '0').
Time Complexity: O(M * N) where M is rows and N is columns.
Space Complexity: O(M * N) for the worst-case recursion stack.
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
                    
        return islands
