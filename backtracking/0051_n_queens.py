"""
Problem: N-Queens
LeetCode #: 51
Difficulty: Hard
Link: https://leetcode.com/problems/n-queens/

Approach: Backtracking placing one queen per row while tracking attacked columns, 
          positive diagonals (row + col), and negative diagonals (row - col).
Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print("N = 4 Solutions:")
    for solution in sol.solveNQueens(4):
        for row in solution:
            print(row)
        print()
