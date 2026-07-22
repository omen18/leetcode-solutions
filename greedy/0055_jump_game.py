"""
Problem: Jump Game
LeetCode #: 55
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game/

Approach: Track the maximum reachable index while iterating through the array. Return False if current index exceeds max reachable index.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + n)
        return True
