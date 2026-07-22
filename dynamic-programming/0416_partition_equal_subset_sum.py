"""
Problem: Partition Equal Subset Sum
LeetCode #: 416
Difficulty: Medium
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Approach: 0/1 Knapsack Dynamic Programming targeting half of total array sum using bit manipulation or boolean set.
Time Complexity: O(N * target)
Space Complexity: O(target)
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        dp = 1  # bit set representing achievable sums
        for num in nums:
            dp |= (dp << num)
            
        return bool((dp >> target) & 1)
