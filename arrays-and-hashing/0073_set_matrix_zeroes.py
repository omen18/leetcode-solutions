"""
Problem: Set Matrix Zeroes
LeetCode #: 73
Difficulty: Medium
Link: https://leetcode.com/problems/set-matrix-zeroes/

Approach: Use first row and first column as markers for zeroing out remaining elements, using single flag for row 0.
Time Complexity: O(M * N) where M is rows and N is columns.
Space Complexity: O(1) auxiliary space.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_zero = True
                    else:
                        matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0
