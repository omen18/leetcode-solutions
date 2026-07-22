"""
Problem: Maximum Subarray
LeetCode #: 53
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Approach: Kadane's Algorithm - Keep track of maximum subarray sum ending at current index.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        curr_max = nums[0]
        
        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            max_so_far = max(max_so_far, curr_max)
            
        return max_so_far
