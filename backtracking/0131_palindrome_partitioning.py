"""
Problem: Palindrome Partitioning
LeetCode #: 131
Difficulty: Medium
Link: https://leetcode.com/problems/palindrome-partitioning/

Approach: Backtracking. At each position start, split s into candidate substring s[start:end]. If s[start:end] is a palindrome, recurse on remaining string from index end.
Time Complexity: O(N * 2^N)
Space Complexity: O(N) for recursion stack.
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, current: List[str]) -> None:
            if start == len(s):
                result.append(list(current))
                return
            
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    current.append(sub)
                    backtrack(end, current)
                    current.pop()
                    
        backtrack(0, [])
        return result
