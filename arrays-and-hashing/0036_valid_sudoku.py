"""
Problem: Valid Sudoku
LeetCode #: 36
Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

Approach: Maintain hash sets for each row, column, and 3x3 box to detect duplicate numbers.
Time Complexity: O(1) since board size is fixed 9x9.
Space Complexity: O(1) space to store set entries for 9x9 board.
"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_idx = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
