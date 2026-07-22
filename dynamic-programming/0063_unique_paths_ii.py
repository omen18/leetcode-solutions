"""
Problem: Unique Paths II
LeetCode #: 63
Difficulty: Medium
Link: https://leetcode.com/problems/unique-paths-ii/

Approach: 1D Dynamic Programming tracking reachable paths while handling obstacles.
Time Complexity: O(m * n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
                    
        return dp[-1]
