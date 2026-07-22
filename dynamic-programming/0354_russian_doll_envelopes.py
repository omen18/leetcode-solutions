"""
Problem: Russian Doll Envelopes
LeetCode #: 354
Difficulty: Hard
Link: https://leetcode.com/problems/russian-doll-envelopes/

Approach: Sort envelopes by width ascending and height descending, then find LIS on heights using binary search.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        tails = []
        for _, h in envelopes:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
                
        return len(tails)
