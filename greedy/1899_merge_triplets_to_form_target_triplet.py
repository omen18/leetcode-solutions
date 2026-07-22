"""
Problem: Merge Triplets to Form Target Triplet
LeetCode #: 1899
Difficulty: Medium
Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

Approach: Ignore triplets with any value exceeding target[i]. Track reachable target elements across valid triplets. Return True if all target elements are matched.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False, False, False]
        
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i in range(3):
                    if t[i] == target[i]:
                        found[i] = True
                        
        return all(found)
