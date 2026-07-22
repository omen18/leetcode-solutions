"""
Problem: Minimum Insertion Steps to Make a String Palindrome
LeetCode #: 1312
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Approach: Dynamic Programming (Longest Palindromic Subsequence). The minimum number of insertions needed
is equal to `len(s) - LPS(s)`. `LPS(s)` is equivalent to the Longest Common Subsequence of `s` and `reversed(s)`.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s_rev = s[::-1]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if s[i - 1] == s_rev[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        lps_length = dp[n]
        return n - lps_length
