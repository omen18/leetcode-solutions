"""
Problem: Min Cost Climbing Stairs
LeetCode #: 746
Difficulty: Easy
Link: https://leetcode.com/problems/min-cost-climbing-stairs/

Approach: Dynamic Programming - Recurrence dp[i] = cost[i] + min(dp[i-1], dp[i-2]) using two state variables.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second = 0, 0
        for c in cost:
            first, second = second, c + min(first, second)
        return min(first, second)
