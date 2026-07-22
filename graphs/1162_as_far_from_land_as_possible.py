"""
Problem: As Far from Land as Possible
LeetCode #: 1162
Difficulty: Medium
Link: https://leetcode.com/problems/as-far-from-land-as-possible/

Approach: Multi-source BFS starting simultaneously from all land cells ('1'). The last water cell ('0') visited by BFS will have the maximum Manhattan distance to any land cell.
Time Complexity: O(N^2) where N is the grid size.
Space Complexity: O(N^2) for the queue.
"""

from typing import List
from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if len(queue) == 0 or len(queue) == n * n:
            return -1

        distance = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))

        return distance
