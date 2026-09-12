"""
Problem: Divide Two Integers
LeetCode #: 29
Difficulty: Medium
Link: https://leetcode.com/problems/divide-two-integers/

Approach: Exponential bit-shifting subtraction without multiplication or division.
Time Complexity: O(log^2 n)
Space Complexity: O(1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        negative = (dividend < 0) ^ (divisor < 0)
        dvd, dvs = abs(dividend), abs(divisor)
        quotient = 0
        while dvd >= dvs:
            temp, mult = dvs, 1
            while dvd >= (temp << 1):
                temp <<= 1
                mult <<= 1
            dvd -= temp
            quotient += mult
        return -quotient if negative else quotient


if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3))   # 3
    print(sol.divide(7, -3))  # -2
