"""
Problem: Nth Magical Number
LeetCode #: 878
Difficulty: Hard
Link: https://leetcode.com/problems/nth-magical-number/

Approach: Binary search on value x in range [1, n * min(a, b)]. Number of magical numbers <= x is given by x // a + x // b - x // lcm(a, b). Find smallest x where count >= n.
Time Complexity: O(log(n * min(a, b)))
Space Complexity: O(1)
"""

import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        lcm = (a * b) // math.gcd(a, b)

        left, right = 1, n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b - mid // lcm

            if count >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD
