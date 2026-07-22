"""
Problem: Largest Plus Sign
LeetCode #: 764
Difficulty: Medium
Link: https://leetcode.com/problems/largest-plus-sign/

Approach: 2D Dynamic Programming. Initialize an N x N grid with N (max possible distance). Set mine locations to 0.
Traverse each row and column in left-to-right/right-to-left and top-to-bottom/bottom-to-top passes to compute
the maximum consecutive ones in all four directions. Take the minimum across all 4 directions for each cell.
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n] * n for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0

        for i in range(n):
            left = right = top = bottom = 0
            for j, k in zip(range(n), reversed(range(n))):
                left = left + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], left)

                right = right + 1 if grid[i][k] != 0 else 0
                grid[i][k] = min(grid[i][k], right)

                top = top + 1 if grid[j][i] != 0 else 0
                grid[j][i] = min(grid[j][i], top)

                bottom = bottom + 1 if grid[k][i] != 0 else 0
                grid[k][i] = min(grid[k][i], bottom)

        res = 0
        for i in range(n):
            for j in range(n):
                res = max(res, grid[i][j])
        return res
