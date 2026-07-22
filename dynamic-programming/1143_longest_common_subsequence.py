"""
Problem: Longest Common Subsequence
LeetCode #: 1143
Difficulty: Medium
Link: https://leetcode.com/problems/longest-common-subsequence/

Approach: 2D Dynamic Programming with 1D space optimization.
`dp[j]` tracks the longest common subsequence of `text1[:i]` and `text2[:j]`.
If `text1[i-1] == text2[j-1]`, `dp[j] = 1 + prev_dp[j-1]`.
Otherwise, `dp[j] = max(dp[j], dp[j-1])`.
Time Complexity: O(M * N) where M = len(text1), N = len(text2)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n]
