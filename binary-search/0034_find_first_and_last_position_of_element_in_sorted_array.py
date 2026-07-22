"""
Problem: Find First and Last Position of Element in Sorted Array
LeetCode #: 34
Difficulty: Medium
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Approach: Use binary search twice (bisect_left and bisect_right - 1) to locate the first and last indices of target.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = bisect.bisect_left(nums, target)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        right_idx = bisect.bisect_right(nums, target) - 1
        return [left_idx, right_idx]
