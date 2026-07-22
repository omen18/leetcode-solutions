"""
Problem: Monotone Increasing Digits
LeetCode #: 738
Difficulty: Medium
Link: https://leetcode.com/problems/monotone-increasing-digits/

Approach: Scan digits from right to left. When digits[i-1] > digits[i], decrement digits[i-1] and set all following digits to 9.
Time Complexity: O(D) where D is the number of digits
Space Complexity: O(D)
"""

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        marker = len(digits)
        
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i
                
        for i in range(marker, len(digits)):
            digits[i] = '9'
            
        return int(''.join(digits))
