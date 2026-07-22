"""
Problem: Delete Operation for Two Strings
LeetCode #: 583
Difficulty: Medium
Link: https://leetcode.com/problems/delete-operation-for-two-strings/

Approach: Dynamic Programming computing Longest Common Subsequence (LCS) to calculate minimum deletions.
Time Complexity: O(m * n)
Space Complexity: O(n)
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = dp[j - 1] + 1
                else:
                    curr[j] = max(dp[j], curr[j - 1])
            dp = curr
            
        lcs = dp[n]
        return m + n - 2 * lcs
