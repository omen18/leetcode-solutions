"""
Problem: 2 Keys Keyboard
LeetCode #: 650
Difficulty: Medium
Link: https://leetcode.com/problems/2-keys-keyboard/

Approach: Prime Factorization / Dynamic Programming - Minimum operations to obtain n 'A's equals the sum of its prime factors.
Time Complexity: O(sqrt(N))
Space Complexity: O(1)
"""


class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
