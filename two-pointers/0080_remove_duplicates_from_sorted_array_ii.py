"""
Problem: Remove Duplicates from Sorted Array II
LeetCode #: 80
Difficulty: Medium
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

Approach: Maintain a write pointer `k`. Iterate with read pointer; place current element at `k` if `k < 2` or current element is greater than `nums[k-2]`.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
