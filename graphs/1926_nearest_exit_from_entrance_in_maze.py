"""
Problem: Nearest Exit from Entrance in Maze
LeetCode #: 1926
Difficulty: Medium
Link: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

Approach: Grid BFS for shortest path.
Perform BFS starting from entrance. The first reachable empty cell ('.') on the grid boundary
that is not the entrance itself is the nearest exit.

Time Complexity: O(R * C) where R and C are rows and columns of maze.
Space Complexity: O(R * C) for queue and grid modifications.
"""

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_r, start_c = entrance[0], entrance[1]

        queue = deque([(start_r, start_c, 0)])
        maze[start_r][start_c] = "+"  # Mark as visited in-place

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return dist + 1

                    maze[nr][nc] = "+"
                    queue.append((nr, nc, dist + 1))

        return -1
