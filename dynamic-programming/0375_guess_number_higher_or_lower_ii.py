"""
Problem: Guess Number Higher or Lower II
LeetCode #: 375
Difficulty: Medium
Link: https://leetcode.com/problems/guess-number-higher-or-lower-ii/

Approach: Interval Dynamic Programming (Minimax) - dp[i][j] is min cost to guarantee win for range [i, j].
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                min_cost = float('inf')
                for x in range(i, j):
                    cost = x + max(dp[i][x - 1], dp[x + 1][j])
                    if cost < min_cost:
                        min_cost = cost
                dp[i][j] = min_cost
                
        return dp[1][n]
