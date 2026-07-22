"""
Problem: Stone Game II
LeetCode #: 1140
Difficulty: Medium
Link: https://leetcode.com/problems/stone-game-ii/

Approach: Dynamic Programming / Minimax with Memoization. Precalculate suffix sums.
`dp(i, M)` computes the maximum stones the current player can take starting from index `i` with parameter `M`.
The current player picks `X` piles (`1 <= X <= 2M`), leaving the opponent `dp(i + X, max(M, X))`.
The current player's total is `suffix_sum[i] - dp(i + X, max(M, X))`.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]

            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - dp(i + x, max(m, x)))
            return res

        return dp(0, 1)
