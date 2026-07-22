"""
Problem: Repeated DNA Sequences
LeetCode #: 187
Difficulty: Medium
Link: https://leetcode.com/problems/repeated-dna-sequences/

Approach: Sliding window of fixed length 10. Track seen 10-letter substrings using hash set and collect those appearing more than once.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()

        for i in range(len(s) - 9):
            sub = s[i:i + 10]
            if sub in seen:
                res.add(sub)
            else:
                seen.add(sub)

        return list(res)
