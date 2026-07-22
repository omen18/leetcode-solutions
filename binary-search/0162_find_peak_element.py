"""
Problem: Find Peak Element
LeetCode #: 162
Difficulty: Medium
Link: https://leetcode.com/problems/find-peak-element/

Approach: Binary search. Compare nums[mid] with nums[mid + 1]. If nums[mid] < nums[mid + 1], a peak must exist in the right half; otherwise in the left half (including mid).
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
