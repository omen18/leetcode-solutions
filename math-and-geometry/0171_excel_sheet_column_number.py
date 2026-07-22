"""
Problem: Excel Sheet Column Number
LeetCode #: 171
Difficulty: Easy
Link: https://leetcode.com/problems/excel-sheet-column-number/

Approach: Positional base-26 expansion from left to right. Multiply running accumulator by 26 and add position value (ord(char) - ord('A') + 1).
Time Complexity: O(n) where n is string length.
Space Complexity: O(1)
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            result = result * 26 + val
        return result
