"""
Problem: Letter Case Permutation
LeetCode #: 784
Difficulty: Medium
Link: https://leetcode.com/problems/letter-case-permutation/

Approach: Backtracking. Iterate through input string: if character is a digit, include as-is and recurse; if a letter, branch into both lowercase and uppercase variations.
Time Complexity: O(N * 2^K) where K is number of letters in string s.
Space Complexity: O(N * 2^K) for storing result permutations.
"""

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        
        def backtrack(index: int, current: List[str]) -> None:
            if index == len(s):
                result.append("".join(current))
                return
            
            char = s[index]
            if char.isalpha():
                current.append(char.lower())
                backtrack(index + 1, current)
                current.pop()
                
                current.append(char.upper())
                backtrack(index + 1, current)
                current.pop()
            else:
                current.append(char)
                backtrack(index + 1, current)
                current.pop()
                
        backtrack(0, [])
        return result
