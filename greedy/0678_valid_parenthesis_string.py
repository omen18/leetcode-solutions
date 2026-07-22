"""
Problem: Valid Parenthesis String
LeetCode #: 678
Difficulty: Medium
Link: https://leetcode.com/problems/valid-parenthesis-string/

Approach: Track the minimum and maximum possible open parenthesis counts. Return True if min open count reaches 0 at the end.
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # '*'
                min_open -= 1
                max_open += 1
                
            if max_open < 0:
                return False
            min_open = max(min_open, 0)
            
        return min_open == 0
