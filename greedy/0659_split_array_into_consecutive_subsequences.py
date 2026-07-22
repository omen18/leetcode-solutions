"""
Problem: Split Array into Consecutive Subsequences
LeetCode #: 659
Difficulty: Medium
Link: https://leetcode.com/problems/split-array-into-consecutive-subsequences/

Approach: Use frequency map and sequence tails map. For each number, greedily append to an existing subsequence of length >= 3 if available, or create a new 3-element subsequence.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import Counter, defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        tails = defaultdict(int)
        
        for x in nums:
            if count[x] == 0:
                continue
            if tails[x - 1] > 0:
                tails[x - 1] -= 1
                tails[x] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x + 1] -= 1
                count[x + 2] -= 1
                tails[x + 2] += 1
            else:
                return False
            count[x] -= 1
            
        return True
