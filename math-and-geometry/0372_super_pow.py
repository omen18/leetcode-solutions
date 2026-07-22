"""
Problem: Super Pow
LeetCode #: 372
Difficulty: Medium
Link: https://leetcode.com/problems/super-pow/

Approach: Modular exponentiation using Horner's method and property (x * y) % m = ((x % m) * (y % m)) % m.
Time Complexity: O(len(b))
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        result = 1

        for digit in b:
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD

        return result
