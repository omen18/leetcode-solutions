"""
Problem: Split a String Into the Max Number of Unique Substrings
LeetCode #: 1593
Difficulty: Medium
Link: https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

Approach: Backtracking. Recursively partition string into substrings using a hash set to track previously seen substrings. Return maximum number of unique splits achievable.
Time Complexity: O(2^N * N)
Space Complexity: O(N) for recursion stack and set.
"""

from typing import List

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        
        def backtrack(start: int) -> int:
            if start == len(s):
                return 0
            
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if sub not in seen:
                    seen.add(sub)
                    max_splits = max(max_splits, 1 + backtrack(end))
                    seen.remove(sub)
                    
            return max_splits
        
        return backtrack(0)
