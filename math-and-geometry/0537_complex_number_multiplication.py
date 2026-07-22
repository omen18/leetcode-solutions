"""
Problem: Complex Number Multiplication
LeetCode #: 537
Difficulty: Medium
Link: https://leetcode.com/problems/complex-number-multiplication/

Approach: Parse real and imaginary components, then apply standard complex multiplication (a+bi)(c+di) = (ac-bd) + (ad+bc)i.
Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split("+"))
        c, d = map(int, num2[:-1].split("+"))

        real = a * c - b * d
        imag = a * d + b * c

        return f"{real}+{imag}i"
