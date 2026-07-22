"""
Problem: Find All Duplicates in an Array
LeetCode #: 442
Difficulty: Medium
Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

Approach: Use array indices as hash keys by negating values at index abs(val) - 1. A negative value indicates prior visit.
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(1) extra space (modifying input in-place).
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return res
