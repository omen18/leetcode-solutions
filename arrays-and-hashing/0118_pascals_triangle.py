"""
Problem: Pascal's Triangle
LeetCode #: 118
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle/

Approach: Generate each row iteratively where element [i][j] = [i-1][j-1] + [i-1][j].
Time Complexity: O(numRows^2)
Space Complexity: O(numRows^2)
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
