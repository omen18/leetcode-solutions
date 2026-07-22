"""
Problem: Shortest Path in Binary Matrix
LeetCode #: 1091
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

Approach: Breadth-First Search (BFS) in 8 directions from start cell (0, 0) to destination (n-1, n-1). Check bounds and 0-value cells.
Time Complexity: O(N^2) where N is the grid side length.
Space Complexity: O(N^2) for BFS queue and visited tracking.
"""

from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        if n == 1:
            return 1

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    if nr == n - 1 and nc == n - 1:
                        return dist + 1
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))

        return -1
