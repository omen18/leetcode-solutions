"""
Problem: Two City Scheduling
LeetCode #: 1029
Difficulty: Medium
Link: https://leetcode.com/problems/two-city-scheduling/

Approach: Sort people by the difference (costA - costB). Send the first N people to City A and the remaining N people to City B.
Time Complexity: O(N log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total_cost = 0
        
        for i in range(n):
            total_cost += costs[i][0]
        for i in range(n, 2 * n):
            total_cost += costs[i][1]
            
        return total_cost
