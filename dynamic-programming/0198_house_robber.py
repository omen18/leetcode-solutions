"""
Problem: House Robber
LeetCode #: 198
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

Approach: Dynamic Programming storing maximum money robbed up to previous two houses.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1
        return prev1
