"""
Problem: Target Sum
LeetCode #: 494
Difficulty: Medium
Link: https://leetcode.com/problems/target-sum/

Approach: Mathematical reduction to Subset Sum 0/1 Knapsack DP problem.
Time Complexity: O(N * S) where S is (sum(nums) + target) // 2
Space Complexity: O(S)
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0
            
        subset_sum = (total_sum + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] += dp[i - num]
                
        return dp[subset_sum]
