"""
Problem: Splitting a String Into Descending Consecutive Values
LeetCode #: 1849
Difficulty: Medium
Link: https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

Approach: Backtracking. Recursively slice candidate numbers from string s and check if each subsequent numerical value is strictly equal to (previous - 1). Requires at least 2 parts.
Time Complexity: O(2^N)
Space Complexity: O(N) for recursion stack.
"""

from typing import List

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(start: int, prev_val: int, count: int) -> bool:
            if start == len(s):
                return count >= 2
            
            for end in range(start + 1, len(s) + 1):
                val = int(s[start:end])
                if prev_val == -1 or val == prev_val - 1:
                    if backtrack(end, val, count + 1):
                        return True
                elif prev_val != -1 and val > prev_val - 1:
                    break
                    
            return False
        
        return backtrack(0, -1, 0)
