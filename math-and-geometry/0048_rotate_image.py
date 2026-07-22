"""
Problem: Rotate Image
LeetCode #: 48
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/

Approach: Transpose the matrix in-place and then reverse each row.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
