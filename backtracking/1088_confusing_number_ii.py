"""
Problem: Confusing Number II
LeetCode #: 1088
Difficulty: Hard
Link: https://leetcode.com/problems/confusing-number-ii/

Approach: Backtracking / Digit Generation. Valid digit set: {0, 1, 6, 8, 9}. Recursively construct numbers up to N, maintaining rotated value in parallel. Count constructed numbers where value != rotated value.
Time Complexity: O(5^D) where D is number of digits in N (D <= 10).
Space Complexity: O(D) for recursion stack.
"""

from typing import List

class Solution:
    def confusingNumberII(self, n: int) -> int:
        rotate_map = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        valid_digits = [0, 1, 6, 8, 9]
        count = 0
        
        def backtrack(curr: int, rotated: int, digit_place: int) -> None:
            nonlocal count
            if curr > n:
                return
            
            if curr != 0 and curr != rotated:
                count += 1
                
            for d in valid_digits:
                if curr == 0 and d == 0:
                    continue
                next_curr = curr * 10 + d
                if next_curr > n:
                    break
                next_rotated = rotate_map[d] * digit_place + rotated
                backtrack(next_curr, next_rotated, digit_place * 10)
                
        backtrack(0, 0, 1)
        return count
