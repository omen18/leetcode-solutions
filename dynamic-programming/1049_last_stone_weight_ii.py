"""
Problem: Last Stone Weight II
LeetCode #: 1049
Difficulty: Medium
Link: https://leetcode.com/problems/last-stone-weight-ii/

Approach: 0/1 Knapsack problem variant. Partition stones into two groups such that the difference between
their sums is minimized. Find maximum sum `S` of a subset of stones such that `S <= total_sum // 2`.
The answer will be `total_sum - 2 * S`.
Time Complexity: O(N * S) where S = sum(stones) // 2
Space Complexity: O(S)
"""

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2

        dp = [True] + [False] * target

        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]

        for j in range(target, -1, -1):
            if dp[j]:
                return total_sum - 2 * j

        return 0
