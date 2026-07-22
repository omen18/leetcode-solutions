"""
Problem: House Robber II
LeetCode #: 213
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber-ii/

Approach: Dynamic Programming solving two linear House Robber subproblems (excluding first or last element).
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(arr: List[int]) -> int:
            prev1, prev2 = 0, 0
            for num in arr:
                prev1, prev2 = max(prev2 + num, prev1), prev1
            return prev1
            
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
