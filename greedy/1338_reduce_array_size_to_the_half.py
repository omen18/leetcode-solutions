"""
Problem: Reduce Array Size to The Half
LeetCode #: 1338
Difficulty: Medium
Link: https://leetcode.com/problems/reduce-array-size-to-the-half/

Approach: Count frequency of each number. Sort frequencies descending and greedily pick the largest frequencies until at least half the array size is removed.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        target = len(arr) // 2
        removed = 0
        set_size = 0
        
        for count in sorted(freq.values(), reverse=True):
            removed += count
            set_size += 1
            if removed >= target:
                break
                
        return set_size
