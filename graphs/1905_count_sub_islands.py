"""
Problem: Count Sub Islands
LeetCode #: 1905
Difficulty: Medium
Link: https://leetcode.com/problems/count-sub-islands/

Approach: Perform DFS on each island in grid2. Validate whether all land cells of that island overlap with land cells ('1') in grid1. Increment counter for valid sub-islands.
Time Complexity: O(M * N) where M and N are grid dimensions.
Space Complexity: O(M * N) for recursion stack.
"""

from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r: int, c: int) -> bool:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] != 1:
                return True

            grid2[r][c] = 0  # mark visited
            is_sub = (grid1[r][c] == 1)

            res1 = dfs(r + 1, c)
            res2 = dfs(r - 1, c)
            res3 = dfs(r, c + 1)
            res4 = dfs(r, c - 1)

            return is_sub and res1 and res2 and res3 and res4

        sub_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        sub_islands += 1

        return sub_islands
