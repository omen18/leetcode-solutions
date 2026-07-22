"""
Problem: Soup Servings
LeetCode #: 808
Difficulty: Medium
Link: https://leetcode.com/problems/soup-servings/

Approach: Dynamic Programming with Memoization. For large N (N >= 4800), the probability approaches 1.0.
For smaller N, convert units by dividing by 25 (rounding up). Recursive DP computes the probability of
Soup A running out first + 0.5 * (probability of A and B running out simultaneously).
Time Complexity: O(1) for N >= 4800; O(N^2) where N <= 192 otherwise
Space Complexity: O(N^2) for memoization grid
"""

import math


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0

        n = math.ceil(n / 25)
        memo = {}

        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            state = (a, b)
            if state in memo:
                return memo[state]

            res = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
            memo[state] = res
            return res

        return dp(n, n)
