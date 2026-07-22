"""
Problem: Pow(x, n)
LeetCode #: 50
Difficulty: Medium
Link: https://leetcode.com/problems/powx-n/

Approach: Binary Exponentiation (Exponentiation by Squaring). Handle negative powers by taking reciprocal 1/x and using positive n.
Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        curr = x

        while n > 0:
            if n % 2 == 1:
                res *= curr
            curr *= curr
            n //= 2

        return res
