"""
Problem: Wiggle Subsequence
LeetCode #: 376
Difficulty: Medium
Link: https://leetcode.com/problems/wiggle-subsequence/

Approach: Count peak and valley transitions by keeping track of the direction of difference between adjacent elements.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
            
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
                
        return count
