"""
Problem: Arithmetic Slices
LeetCode #: 413
Difficulty: Medium
Link: https://leetcode.com/problems/arithmetic-slices/

Approach: Constant space DP adding consecutive differences matched in adjacent triplets.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
            
        total = 0
        curr = 0
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                total += curr
            else:
                curr = 0
                
        return total
