"""
Problem: Excel Sheet Column Title
LeetCode #: 168
Difficulty: Easy
Link: https://leetcode.com/problems/excel-sheet-column-title/

Approach: Base-26 conversion with 1-based indexing. Subtract 1 from columnNumber before taking modulo 26 to map 0 -> 'A', 25 -> 'Z'.
Time Complexity: O(log26(N))
Space Complexity: O(1) auxiliary
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            rem = columnNumber % 26
            res.append(chr(ord('A') + rem))
            columnNumber //= 26

        return "".join(reversed(res))
