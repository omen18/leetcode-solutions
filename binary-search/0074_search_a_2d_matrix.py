"""
Problem: Search a 2D Matrix
LeetCode #: 74
Difficulty: Medium
Link: https://leetcode.com/problems/search-a-2d-matrix/

Approach: Treat the m x n matrix as a flattened sorted 1D array of length m * n and perform standard binary search. Map mid index to row = mid // n and col = mid % n.
Time Complexity: O(log(m * n))
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
