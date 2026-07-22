"""
Problem: Count Numbers with Unique Digits
LeetCode #: 357
Difficulty: Medium
Link: https://leetcode.com/problems/count-numbers-with-unique-digits/

Approach: Combinatorics / Dynamic Programming - For length k, number of unique-digit numbers is 9 * 9 * 8 * ... * (11 - k).
Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
            
        total = 10
        unique_digits = 9
        available_choices = 9
        
        for i in range(2, min(n + 1, 11)):
            unique_digits *= available_choices
            total += unique_digits
            available_choices -= 1
            
        return total
