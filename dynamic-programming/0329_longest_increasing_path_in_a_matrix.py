"""
Problem: Longest Increasing Path in a Matrix
LeetCode #: 329
Difficulty: Hard
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Approach: Dynamic Programming with Memoized DFS. `dp[r][c]` stores the length of the longest increasing path starting at `(r, c)`.
From each cell, recursively explore valid neighbors `(nr, nc)` where `matrix[nr][nc] > matrix[r][c]`.
Time Complexity: O(M * N) where M, N are dimensions of matrix
Space Complexity: O(M * N) for memoization grid and recursion stack
"""

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]

        def dfs(r: int, c: int) -> int:
            if memo[r][c] != 0:
                return memo[r][c]

            max_len = 1
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[r][c] = max_len
            return max_len

        return max(dfs(r, c) for r in range(m) for c in range(n))
