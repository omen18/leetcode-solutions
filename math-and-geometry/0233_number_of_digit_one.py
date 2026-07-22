"""
Problem: Number of Digit One
LeetCode #: 233
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-digit-one/

Approach: Count occurrences of digit '1' at each place value (ones, tens, hundreds, etc.) using digit arithmetic.
Time Complexity: O(log10(N))
Space Complexity: O(1)
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            count += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10

        return count
