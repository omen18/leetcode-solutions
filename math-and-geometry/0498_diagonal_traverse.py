"""
Problem: Diagonal Traverse
LeetCode #: 498
Difficulty: Medium
Link: https://leetcode.com/problems/diagonal-traverse/

Approach: Group elements by diagonal index (row + col) and reverse alternate diagonals.
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])

        result = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(diagonals[d][::-1])
            else:
                result.extend(diagonals[d])

        return result
