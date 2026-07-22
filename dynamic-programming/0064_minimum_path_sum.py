"""
Problem: Minimum Path Sum
LeetCode #: 64
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-path-sum/

Approach: 1D Dynamic Programming optimizing minimum sum path from top-left to bottom-right.
Time Complexity: O(m * n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                
        return dp[-1]
