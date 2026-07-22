"""
Problem: Maximum Bags Full of Rocks
LeetCode #: 2279
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-bags-full-of-rocks/

Approach: Calculate remaining capacity for each bag. Sort remaining capacities ascending and greedily fill bags requiring the fewest additional rocks.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needed = [c - r for c, r in zip(capacity, rocks)]
        needed.sort()
        
        full_bags = 0
        for req in needed:
            if additionalRocks >= req:
                additionalRocks -= req
                full_bags += 1
            else:
                break
                
        return full_bags
