"""
Problem: Paint House
LeetCode #: 256
Difficulty: Medium
Link: https://leetcode.com/problems/paint-house/

Approach: Dynamic Programming - Track minimum cost of painting houses with 3 different colors iteratively.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
            
        r, b, g = 0, 0, 0
        
        for cost_r, cost_b, cost_g in costs:
            new_r = cost_r + min(b, g)
            new_b = cost_b + min(r, g)
            new_g = cost_g + min(r, b)
            r, b, g = new_r, new_b, new_g
            
        return min(r, b, g)
