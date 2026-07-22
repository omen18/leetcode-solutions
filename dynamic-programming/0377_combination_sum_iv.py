"""
Problem: Combination Sum IV
LeetCode #: 377
Difficulty: Medium
Link: https://leetcode.com/problems/combination-sum-iv/

Approach: Dynamic Programming with bottom-up table counting permutations to reach target sum.
Time Complexity: O(target * len(nums))
Space Complexity: O(target)
"""

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]
