"""
Problem: Word Break
LeetCode #: 139
Difficulty: Medium
Link: https://leetcode.com/problems/word-break/

Approach: 1D Dynamic Programming checking substring validity using a hash set.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
                    
        return dp[-1]
