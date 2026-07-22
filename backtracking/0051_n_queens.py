"""
Problem: N-Queens
LeetCode #: 51
Difficulty: Hard
Link: https://leetcode.com/problems/n-queens/

Approach: Backtracking. Place queens row by row while tracking occupied columns, main diagonals (r + c), and anti-diagonals (r - c) using sets. Build board configuration when r == n.
Time Complexity: O(N!)
Space Complexity: O(N) for column and diagonal tracking sets and recursion stack.
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set()  # r + c
        neg_diag = set()  # r - c
        result = []
        board = [["."] * n for _ in range(n)]
        
        def backtrack(r: int) -> None:
            if r == n:
                result.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = 'Q'
                
                backtrack(r + 1)
                
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = '.'
                
        backtrack(0)
        return result
