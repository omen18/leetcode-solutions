"""
Problem: Wiggle Subsequence
LeetCode #: 376
Difficulty: Medium
Link: https://leetcode.com/problems/wiggle-subsequence/

Approach: Dynamic Programming - Maintain length of wiggle sequence ending with positive (up) and negative (down) differences.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
                
        return max(up, down)
