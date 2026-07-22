"""
Problem: Shortest Bridge
LeetCode #: 934
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-bridge/

Approach: Use DFS to find and collect all cells of the first island in a queue while marking them visited. Then run Multi-source BFS level-by-level to find the shortest distance to the second island.
Time Complexity: O(N^2) where N is grid dimension.
Space Complexity: O(N^2) for BFS queue and recursion.
"""

from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        found = False

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return
            grid[r][c] = 2
            queue.append((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        distance = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return distance
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
            distance += 1

        return distance
