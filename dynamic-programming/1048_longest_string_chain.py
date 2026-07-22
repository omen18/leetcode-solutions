"""
Problem: Longest String Chain
LeetCode #: 1048
Difficulty: Medium
Link: https://leetcode.com/problems/longest-string-chain/

Approach: Dynamic Programming with Hash Map - Sort words by length, then check all single-character deletions for predecessors.
Time Complexity: O(N * L^2) where N is number of words and L is maximum word length.
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain = 1
        
        for word in words:
            curr_max = 1
            for i in range(len(word)):
                pred = word[:i] + word[i + 1:]
                if pred in dp:
                    curr_max = max(curr_max, dp[pred] + 1)
            dp[word] = curr_max
            max_chain = max(max_chain, curr_max)
            
        return max_chain
