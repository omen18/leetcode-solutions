"""
Problem: Integer Break
LeetCode #: 343
Difficulty: Medium
Link: https://leetcode.com/problems/integer-break/

Approach: Mathematical optimization using factors of 3 to maximize the product.
Time Complexity: O(log N)
Space Complexity: O(1)
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return (3 ** ((n // 3) - 1)) * 4
        else:
            return (3 ** (n // 3)) * 2
