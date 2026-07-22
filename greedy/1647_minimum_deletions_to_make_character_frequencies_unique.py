"""
Problem: Minimum Deletions to Make Character Frequencies Unique
LeetCode #: 1647
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

Approach: Count character frequencies. For each frequency, decrement it until it becomes unique or reaches 0, tracking total deletions.
Time Complexity: O(N)
Space Complexity: O(K) where K is alphabet size (26)
"""

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = Counter(s)
        seen_freqs = set()
        deletions = 0
        
        for count in freq.values():
            while count > 0 and count in seen_freqs:
                count -= 1
                deletions += 1
            if count > 0:
                seen_freqs.add(count)
                
        return deletions
