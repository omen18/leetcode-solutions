"""
Problem: Surrounded Regions
LeetCode #: 130
Difficulty: Medium
Link: https://leetcode.com/problems/surrounded-regions/

Approach: Boundary DFS/BFS. Start from all 'O's on the border and run DFS/BFS to mark all reachable 'O's as safe (e.g. '#'). Then iterate over the grid: flip remaining 'O's to 'X' (surrounded) and '#' back to 'O' (safe).
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Mark boundary-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Update grid values
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
