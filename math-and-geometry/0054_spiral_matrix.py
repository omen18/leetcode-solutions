"""
Problem: Spiral Matrix
LeetCode #: 54
Difficulty: Medium
Link: https://leetcode.com/problems/spiral-matrix/

Approach: Maintain 4 boundaries (top, bottom, left, right) and traverse in spiral order.
Time Complexity: O(M * N)
Space Complexity: O(1) auxiliary (excluding output array)
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse Right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse Left
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # Traverse Up
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
