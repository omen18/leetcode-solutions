"""
Problem: Container With Most Water
LeetCode #: 11
Difficulty: Medium
Link: https://leetcode.com/problems/container-with-most-water/

Approach: Two pointers starting at opposite ends. At each step, calculate area `(right - left) * min(height[left], height[right])` and update maximum. Move the pointer pointing to the shorter line inward.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            max_water = max(max_water, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
