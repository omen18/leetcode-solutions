"""
Problem: Single Element in a Sorted Array
LeetCode #: 540
Difficulty: Medium
Link: https://leetcode.com/problems/single-element-in-a-sorted-array/

Approach: Binary search on even indices. If nums[mid] == nums[mid ^ 1], the single element lies to the right; otherwise it lies to the left.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
