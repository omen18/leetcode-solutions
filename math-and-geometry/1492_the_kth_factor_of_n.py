"""
Problem: The kth Factor of n
LeetCode #: 1492
Difficulty: Medium
Link: https://leetcode.com/problems/the-kth-factor-of-n/

Approach: Iterate up to sqrt(n) to collect factor pairs, keeping O(sqrt(N)) time.
Time Complexity: O(sqrt(N))
Space Complexity: O(sqrt(N))
"""

import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small_factors = []
        large_factors = []

        for i in range(1, math.isqrt(n) + 1):
            if n % i == 0:
                small_factors.append(i)
                if i * i != n:
                    large_factors.append(n // i)

        factors = small_factors + large_factors[::-1]
        return factors[k - 1] if k <= len(factors) else -1
