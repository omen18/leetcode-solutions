"""
Problem: Maximum Product Subarray
LeetCode #: 152
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-product-subarray/

Approach: DP maintaining current minimum and maximum product at each index to handle negative signs.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = nums[0]
        cur_min, cur_max = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                cur_min, cur_max = cur_max, cur_min
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            res = max(res, cur_max)
            
        return res
