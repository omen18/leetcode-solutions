"""
Problem: Strange Printer
LeetCode #: 664
Difficulty: Hard
Link: https://leetcode.com/problems/strange-printer/

Approach: Interval Dynamic Programming with Memoization.
`dp(i, j)` computes the minimum turns to print substring `s[i..j]`.
- Base case: `i == j` returns 1.
- If `s[i] == s[j]`, the last character can be printed in the same turn as `s[i]`: `dp(i, j) = dp(i, j - 1)`.
- Otherwise, split range at `k` (`i <= k < j`): `dp(i, j) = min(dp(i, k) + dp(k + 1, j))`.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

from functools import lru_cache
from typing import List


class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        # Remove adjacent duplicates
        filtered = []
        for ch in s:
            if not filtered or filtered[-1] != ch:
                filtered.append(ch)

        n = len(filtered)

        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i >= j:
                return 1 if i == j else 0

            res = dp(i, j - 1) + 1
            for k in range(i, j):
                if filtered[k] == filtered[j]:
                    res = min(res, dp(i, k) + dp(k + 1, j - 1))

            return res

        return dp(0, n - 1)
