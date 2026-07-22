"""
Problem: Number of Ways to Form a Target String Given a Dictionary
LeetCode #: 1639
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

Approach: Dynamic Programming - Count character frequencies per column, then match target characters column by column.
Time Complexity: O(W * L + M * L) where W is words count, L is word length, M is target length.
Space Complexity: O(M + L * 26)
"""

from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m = len(target)
        n = len(words[0])
        
        # Precompute character frequencies for each column
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ord(ch) - ord('a')] += 1
                
        # dp[i] represents number of ways to form target[:i]
        dp = [0] * (m + 1)
        dp[0] = 1
        
        for j in range(n):
            for i in range(m, 0, -1):
                char_idx = ord(target[i - 1]) - ord('a')
                count = freq[j][char_idx]
                if count > 0:
                    dp[i] = (dp[i] + dp[i - 1] * count) % MOD
                    
        return dp[m]
