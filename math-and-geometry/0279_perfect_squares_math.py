"""
Problem: Perfect Squares
LeetCode #: 279
Difficulty: Medium
Link: https://leetcode.com/problems/perfect-squares/

Approach: Mathematical solution using Legendre's Three-Square Theorem and Lagrange's Four-Square Theorem.
Time Complexity: O(sqrt(N))
Space Complexity: O(1)
"""

import math


class Solution:
    def numSquares(self, n: int) -> int:
        # Check if n is a perfect square
        if self._isSquare(n):
            return 1

        # Check if n fits 4^a * (8b + 7)
        temp = n
        while temp % 4 == 0:
            temp //= 4
        if temp % 8 == 7:
            return 4

        # Check if n can be represented as sum of 2 perfect squares
        for i in range(1, int(math.isqrt(n)) + 1):
            if self._isSquare(n - i * i):
                return 2

        # Otherwise answer must be 3
        return 3

    def _isSquare(self, n: int) -> bool:
        sq = math.isqrt(n)
        return sq * sq == n
