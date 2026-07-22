"""
Problem: Edit Distance
LeetCode #: 72
Difficulty: Hard
Link: https://leetcode.com/problems/edit-distance/

Approach: Dynamic Programming (Levenshtein Distance).
`dp[j]` represents the edit distance between `word1[:i]` and `word2[:j]`.
- If `word1[i-1] == word2[j-1]`, no operation needed: `dp[j] = prev_dp[j-1]`.
- Otherwise: `1 + min(dp[j] (delete), dp[j-1] (insert), prev_dp[j-1] (replace))`.
Time Complexity: O(M * N) where M = len(word1), N = len(word2)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                prev = temp

        return dp[n]
