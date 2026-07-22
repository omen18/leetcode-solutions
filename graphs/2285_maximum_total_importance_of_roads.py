"""
Problem: Maximum Total Importance of Roads
LeetCode #: 2285
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-total-importance-of-roads/

Approach: Greedy Choice. Calculate the degree (number of connecting roads) for each city. Cities with higher degrees contribute to more total road values, so assign them higher values (1 to n) greedily.
Time Complexity: O(N log N + E)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1

        degree.sort()

        total_importance = 0
        for val, deg in enumerate(degree, 1):
            total_importance += val * deg

        return total_importance
