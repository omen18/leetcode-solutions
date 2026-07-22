"""
Problem: Letter Combinations of a Phone Number
LeetCode #: 17
Difficulty: Medium
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Approach: Backtracking / Depth-First Search. Map digits 2-9 to corresponding letters and recursively build combinations by picking letters for each digit position.
Time Complexity: O(4^N * N) where N is the number of digits.
Space Complexity: O(N) for recursion stack.
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current: List[str]) -> None:
            if index == len(digits):
                result.append("".join(current))
                return
            
            for char in mapping[digits[index]]:
                current.append(char)
                backtrack(index + 1, current)
                current.pop()
                
        backtrack(0, [])
        return result
