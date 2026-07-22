"""
Problem: First Missing Positive
LeetCode #: 41
Difficulty: Hard
Link: https://leetcode.com/problems/first-missing-positive/

Approach: Cycle sort. Place each integer val in range 1..N at index (val - 1) via swaps. First mismatched index i yields (i + 1).
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(1) auxiliary space.
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
