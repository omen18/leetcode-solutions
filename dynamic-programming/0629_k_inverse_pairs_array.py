"""
Problem: K Inverse Pairs Array
LeetCode #: 629
Difficulty: Hard
Link: https://leetcode.com/problems/k-inverse-pairs-array/

Approach: Dynamic Programming with Sliding Window / Prefix Sum optimization.
`dp[i][j]` is the number of array permutations of `1..i` with `j` inverse pairs.
Recurrence: `dp[i][j] = sum(dp[i-1][j - p])` for `0 <= p < i`.
Optimized recurrence: `dp[i][j] = (dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]) % MOD`.
Time Complexity: O(N * K)
Space Complexity: O(K)
"""

from typing import List


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        if k == 0:
            return 1
        if k > n * (n - 1) // 2:
            return 0

        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            next_dp = [0] * (k + 1)
            next_dp[0] = 1
            for j in range(1, k + 1):
                val = (next_dp[j - 1] + dp[j]) % MOD
                if j >= i:
                    val = (val - dp[j - i] + MOD) % MOD
                next_dp[j] = val
            dp = next_dp

        return dp[k]
