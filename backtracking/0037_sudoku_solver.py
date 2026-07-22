"""
Problem: Sudoku Solver
LeetCode #: 37
Difficulty: Hard
Link: https://leetcode.com/problems/sudoku-solver/

Approach: Backtracking with Bitmasks. Maintain bitmasks for rows, columns, and 3x3 sub-boxes to check digit validity in O(1). Recursively fill empty cells, modifying board in-place.
Time Complexity: O(9^(N^2)) bounded by Sudoku constraints (executes in milliseconds with bitwise operations).
Space Complexity: O(1) space bound (81 grid cells recursion depth).
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    digit = int(board[r][c]) - 1
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx] |= mask
                else:
                    empty_cells.append((r, c))
                    
        def backtrack(idx: int) -> bool:
            if idx == len(empty_cells):
                return True
            
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            used = rows[r] | cols[c] | boxes[box_idx]
            
            for digit in range(9):
                mask = 1 << digit
                if not (used & mask):
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_idx] |= mask
                    board[r][c] = str(digit + 1)
                    
                    if backtrack(idx + 1):
                        return True
                    
                    rows[r] ^= mask
                    cols[c] ^= mask
                    boxes[box_idx] ^= mask
                    board[r][c] = '.'
                    
            return False
        
        backtrack(0)
