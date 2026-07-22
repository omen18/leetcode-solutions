"""
Problem: Minimum Cost to Cut a Stick
LeetCode #: 1547
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

Approach: Interval Dynamic Programming - Add boundaries 0 and n, sort cuts, and calculate optimal cut cost for sub-stick [i, j].
Time Complexity: O(C^3) where C is the number of cuts.
Space Complexity: O(C^2)
"""

from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        
        for length in range(2, m):
            for i in range(m - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                dp[i][j] += cuts[j] - cuts[i]
                
        return dp[0][m - 1]
