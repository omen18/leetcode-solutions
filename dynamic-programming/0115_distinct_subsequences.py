"""
Problem: Distinct Subsequences
LeetCode #: 115
Difficulty: Hard
Link: https://leetcode.com/problems/distinct-subsequences/

Approach: Dynamic Programming with 1D space optimization.
`dp[j]` represents the number of distinct subsequences of `s[:i]` that equal `t[:j]`.
Base case: `dp[0] = 1` (empty `t` matches any prefix of `s` in 1 way).
For each char `s[i-1]`, iterate `j` backwards: if `s[i-1] == t[j-1]`, `dp[j] += dp[j-1]`.
Time Complexity: O(M * N) where M = len(s), N = len(t)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]
