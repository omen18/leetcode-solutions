"""
Problem: Add Digits
LeetCode #: 258
Difficulty: Easy
Link: https://leetcode.com/problems/add-digits/

Approach: Digital Root mathematical formula: 1 + (num - 1) % 9 if num > 0 else 0.
Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
