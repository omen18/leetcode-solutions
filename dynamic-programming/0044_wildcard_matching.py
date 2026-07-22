"""
Problem: Wildcard Matching
LeetCode #: 44
Difficulty: Hard
Link: https://leetcode.com/problems/wildcard-matching/

Approach: 2D Dynamic Programming with space optimization.
`dp[j]` tracks whether prefix `s[:i]` matches pattern `p[:j]`.
- If `p[j-1] == '?'` or `p[j-1] == s[i-1]`, `dp[j] = prev_dp[j-1]`.
- If `p[j-1] == '*'`, `dp[j] = dp[j-1]` (matches empty sequence) or `dp[j]` from previous row (matches non-empty sequence).
Time Complexity: O(M * N) where M = len(s), N = len(p)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True

        # Base case: leading '*' in pattern can match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = False
            for j in range(1, n + 1):
                temp = dp[j]
                if p[j - 1] == '*':
                    dp[j] = dp[j] or dp[j - 1]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[j] = prev
                else:
                    dp[j] = False
                prev = temp

        return dp[n]
