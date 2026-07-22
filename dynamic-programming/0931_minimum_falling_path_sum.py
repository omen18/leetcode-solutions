"""
Problem: Minimum Falling Path Sum
LeetCode #: 931
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-falling-path-sum/

Approach: Dynamic Programming. Iterate from the second-to-last row up to the top row.
For each cell `(r, c)`, add the minimum of the three reachable cells in the row below:
`(r+1, c-1)`, `(r+1, c)`, `(r+1, c+1)`. Return the minimum value in the top row.
Time Complexity: O(N^2)
Space Complexity: O(N) or O(1) in-place modification
"""

from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = list(matrix[-1])

        for r in range(n - 2, -1, -1):
            next_dp = [0] * n
            for c in range(n):
                left = dp[c - 1] if c > 0 else float('inf')
                mid = dp[c]
                right = dp[c + 1] if c < n - 1 else float('inf')
                next_dp[c] = matrix[r][c] + min(left, mid, right)
            dp = next_dp

        return min(dp)
