"""
Problem: Triangle
LeetCode #: 120
Difficulty: Medium
Link: https://leetcode.com/problems/triangle/

Approach: Bottom-up Dynamic Programming - Modify minimum path sum row by row from bottom to top.
Time Complexity: O(N^2) where N is the number of rows.
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = list(triangle[-1])
        
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        return dp[0]
