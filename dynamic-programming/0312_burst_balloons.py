"""
Problem: Burst Balloons
LeetCode #: 312
Difficulty: Hard
Link: https://leetcode.com/problems/burst-balloons/

Approach: Range Dynamic Programming. Pad `nums` with 1 at both ends to form `padded = [1] + nums + [1]`.
`dp[i][j]` represents maximum coins gained by bursting all balloons strictly between index `i` and `j`.
Iterate subproblem length `length` from 1 to `n`. For each range `(i, j)`, consider balloon `k` (`i < k < j`)
burst last in range `(i, j)`:
`dp[i][j] = max(dp[i][j], dp[i][k] + padded[i] * padded[k] * padded[j] + dp[k][j])`.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded = [1] + nums + [1]
        n = len(padded)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n - 1):
            for i in range(n - length - 1):
                j = i + length + 1
                for k in range(i + 1, j):
                    coins = padded[i] * padded[k] * padded[j]
                    dp[i][j] = max(dp[i][j], dp[i][k] + coins + dp[k][j])

        return dp[0][n - 1]
