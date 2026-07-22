"""
Problem: Minimum Cost to Make at Least One Valid Path in a Grid
LeetCode #: 1368
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

Approach: 0-1 BFS with Deque. Moving in the direction indicated by the current cell costs 0 (append left), while changing direction costs 1 (append right).
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        queue = deque([(0, 0, 0)])

        while queue:
            cost, r, c = queue.popleft()

            if cost > dist[r][c]:
                continue
            if r == rows - 1 and c == cols - 1:
                return cost

            for d_idx, (dr, dc) in enumerate(dirs, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    weight = 0 if grid[r][c] == d_idx else 1
                    if cost + weight < dist[nr][nc]:
                        dist[nr][nc] = cost + weight
                        if weight == 0:
                            queue.appendleft((cost, nr, nc))
                        else:
                            queue.append((cost + weight, nr, nc))

        return dist[rows - 1][cols - 1]
