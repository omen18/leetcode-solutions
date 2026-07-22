"""
Problem: Find Minimum in Rotated Sorted Array
LeetCode #: 153
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Approach: Binary search by comparing nums[mid] with nums[right]. If nums[mid] > nums[right], minimum lies in the right part; otherwise it lies in the left part (including mid).
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
