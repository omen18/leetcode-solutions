"""
Problem: Unique Paths
LeetCode #: 62
Difficulty: Medium
Link: https://leetcode.com/problems/unique-paths/

Approach: Dynamic Programming with 1D array space optimization where dp[j] stores number of unique paths to cell (i, j).
Time Complexity: O(m * n)
Space Complexity: O(n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
