"""
Problem: Longest Palindromic Subsequence
LeetCode #: 516
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-subsequence/

Approach: 2D Dynamic Programming with space optimization - dp[j] stores LPS length for substring s[i..j].
Time Complexity: O(N^2)
Space Complexity: O(N)
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        
        for i in range(n - 1, -1, -1):
            dp[i] = 1
            prev_diag = 0
            for j in range(i + 1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev_diag + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev_diag = temp
                
        return dp[n - 1]
