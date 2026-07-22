"""
Problem: Perfect Squares
LeetCode #: 279
Difficulty: Medium
Link: https://leetcode.com/problems/perfect-squares/

Approach: 1D Dynamic Programming evaluating minimum perfect squares for each integer up to n.
Time Complexity: O(n * sqrt(n))
Space Complexity: O(n)
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        
        for i in range(1, n + 1):
            for sq in squares:
                if sq > i:
                    break
                dp[i] = min(dp[i], dp[i - sq] + 1)
                
        return dp[n]
