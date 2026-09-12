"""
Problem: Game of Life
LeetCode #: 289
Difficulty: Medium
Link: https://leetcode.com/problems/game-of-life/

Approach: In-place simulation with state flags for live->dead and dead->live transitions.
Time Complexity: O(m * n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for r in range(m):
            for c in range(n):
                live_neighbors = sum(
                    board[r + dr][c + dc] in (1, 2)
                    for dr, dc in neighbors
                    if 0 <= r + dr < m and 0 <= c + dc < n
                )
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2  # was alive, now dead
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 3  # was dead, now alive

        for r in range(m):
            for c in range(n):
                board[r][c] = 1 if board[r][c] in (1, 3) else 0


if __name__ == "__main__":
    sol = Solution()
    b = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.gameOfLife(b)
    print(b[0])
