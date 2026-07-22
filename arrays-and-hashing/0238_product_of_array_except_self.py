"""
Problem: Product of Array Except Self
LeetCode #: 238
Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

Approach: Calculate prefix products in output array from left to right, then multiply by postfix products from right to left in a second pass.
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(1) extra space excluding output array.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
