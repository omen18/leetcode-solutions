"""
Problem: Regular Expression Matching
LeetCode #: 10
Difficulty: Hard
Link: https://leetcode.com/problems/regular-expression-matching/

Approach: 2D Dynamic Programming. `dp[i][j]` indicates if `s[:i]` matches pattern `p[:j]`.
- If `p[j-1] == s[i-1]` or `p[j-1] == '.'`, `dp[i][j] = dp[i-1][j-1]`.
- If `p[j-1] == '*'`:
  - Zero occurrences of character before '*': `dp[i][j] = dp[i][j-2]`.
  - One or more occurrences (if preceding char matches `s[i-1]`): `dp[i][j] |= dp[i-1][j]`.
Time Complexity: O(M * N) where M = len(s), N = len(p)
Space Complexity: O(M * N)
"""

from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle empty string matching patterns like a*, a*b*, etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Zero occurrence of preceding element
                    dp[i][j] = dp[i][j - 2]
                    # One or more occurrences if preceding element matches s[i-1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
