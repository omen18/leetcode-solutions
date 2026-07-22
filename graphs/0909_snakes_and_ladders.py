"""
Problem: Snakes and Ladders
LeetCode #: 909
Difficulty: Medium
Link: https://leetcode.com/problems/snakes-and-ladders/

Approach: BFS for Shortest Path. Convert 1-based square index to 2D board coordinates (boustrophedon pattern). Perform BFS from square 1 to find the minimum number of rolls to reach square n^2.
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coords(square: int) -> tuple:
            r = (square - 1) // n
            c = (square - 1) % n
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        visited = set([1])
        queue = deque([(1, 0)])  # (square, moves)

        while queue:
            curr, moves = queue.popleft()
            if curr == n * n:
                return moves

            for die in range(1, 7):
                nxt = curr + die
                if nxt > n * n:
                    break

                r, c = get_coords(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt

                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1
