"""
Problem: Search in Rotated Sorted Array
LeetCode #: 33
Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Approach: Binary search by identifying which half (left or right) is sorted, then checking if the target lies within the sorted range.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
