"""
Problem: Integer Break
LeetCode #: 343
Difficulty: Medium
Link: https://leetcode.com/problems/integer-break/

Approach: Dynamic Programming evaluating maximum product breakdown for numbers up to n.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                
        return dp[n]
