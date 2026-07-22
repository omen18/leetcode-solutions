"""
Problem: Minimum Cost to Merge Stones
LeetCode #: 1000
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-cost-to-merge-stones/

Approach: Interval Dynamic Programming.
Merging `n` stones into 1 pile using `k` stones per merge is possible if and only if `(n - 1) % (k - 1) == 0`.
`dp[i][j]` represents the minimum cost to merge `stones[i..j]` into as few piles as possible.
For range `(i, j)`, step by `k - 1`: `dp[i][j] = min(dp[i][m] + dp[m + 1][j])`.
If `(j - i) % (k - 1) == 0`, merging into 1 final pile adds `sum(stones[i..j])`.
Time Complexity: O(N^3 / K)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for m in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])

                if (j - i) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]

        return int(dp[0][n - 1])
