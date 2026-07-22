"""
Problem: Ones and Zeroes
LeetCode #: 474
Difficulty: Medium
Link: https://leetcode.com/problems/ones-and-zeroes/

Approach: 2D 0/1 Knapsack Dynamic Programming storing maximum subsets for zeros and ones limits.
Time Complexity: O(L * m * n) where L is len(strs)
Space Complexity: O(m * n)
"""

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                    
        return dp[m][n]
