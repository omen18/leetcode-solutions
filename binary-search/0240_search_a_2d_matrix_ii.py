"""
Problem: Search a 2D Matrix II
LeetCode #: 240
Difficulty: Medium
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/

Approach: Start from top-right corner; move left if too large, move down if too small.
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(sol.searchMatrix(mat, 5))  # True
