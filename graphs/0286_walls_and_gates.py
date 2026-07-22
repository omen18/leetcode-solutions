"""
Problem: Walls and Gates
LeetCode #: 286
Difficulty: Medium
Link: https://leetcode.com/problems/walls-and-gates/

Approach: Multi-source Breadth-First Search (BFS) starting simultaneously from all gates (val 0). Traverse neighboring empty rooms (val 2147483647) level-by-level, updating shortest distance in-place.
Time Complexity: O(M * N) where M and N are grid dimensions.
Space Complexity: O(M * N) for the queue.
"""

from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))
