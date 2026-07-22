"""
Problem: Ugly Number II
LeetCode #: 264
Difficulty: Medium
Link: https://leetcode.com/problems/ugly-number-ii/

Approach: Three-pointer Dynamic Programming generating ugly numbers sequentially.
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            next2, next3, next5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(next2, next3, next5)
            if dp[i] == next2:
                p2 += 1
            if dp[i] == next3:
                p3 += 1
            if dp[i] == next5:
                p5 += 1
                
        return dp[-1]
