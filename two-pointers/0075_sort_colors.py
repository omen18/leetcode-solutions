"""
Problem: Sort Colors
LeetCode #: 75
Difficulty: Medium
Link: https://leetcode.com/problems/sort-colors/

Approach: Dutch National Flag algorithm with three pointers (`low`, `mid`, `high`). Partition array into 0s, 1s, and 2s in a single pass in-place.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
