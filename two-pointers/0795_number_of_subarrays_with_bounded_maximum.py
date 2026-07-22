"""
Problem: Number of Subarrays with Bounded Maximum
LeetCode #: 795
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

Approach: Maintain pointers `left` (start of valid range) and `count` (number of valid subarrays ending at current index). For num > right, reset range. For left <= num <= right, update count = i - left + 1. For num < left, count remains same.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        l = -1
        r = -1

        for i, num in enumerate(nums):
            if num > right:
                l = i
            if num >= left:
                r = i
            ans += r - l

        return ans
