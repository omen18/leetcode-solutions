"""
Problem: Range Sum Query 2D - Immutable
LeetCode #: 304
Difficulty: Medium
Link: https://leetcode.com/problems/range-sum-query-2d-immutable/

Approach: Construct 2D prefix sum array where pref[r+1][c+1] stores sum of submatrix from (0,0) to (r,c).
Time Complexity: O(M * N) for initialization, O(1) per sumRegion query.
Space Complexity: O(M * N) to store prefix sum matrix.
"""

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.pref = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                self.pref[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.pref[r][c + 1]
                    + self.pref[r + 1][c]
                    - self.pref[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.pref[row2 + 1][col2 + 1]
            - self.pref[row1][col2 + 1]
            - self.pref[row2 + 1][col1]
            + self.pref[row1][col1]
        )
