"""
Problem: Sum of Two Integers
LeetCode #: 371
Difficulty: Medium
Link: https://leetcode.com/problems/sum-of-two-integers/

Approach: Bitwise addition using XOR for uncarried sum and AND shifted left by 1 for carry, bounded to 32 bits.
Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)
