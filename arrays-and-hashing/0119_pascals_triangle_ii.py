"""
Problem: Pascal's Triangle II
LeetCode #: 119
Difficulty: Easy
Link: https://leetcode.com/problems/pascals-triangle-ii/

Approach: Build row in-place backwards to achieve O(k) memory.
Time Complexity: O(k^2)
Space Complexity: O(k)
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row


if __name__ == "__main__":
    sol = Solution()
    print(sol.getRow(3))  # [1, 3, 3, 1]
    print(sol.getRow(0))  # [1]
