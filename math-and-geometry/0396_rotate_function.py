"""
Problem: Rotate Function
LeetCode #: 396
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-function/

Approach: Mathematical relation F(k) = F(k-1) + sum(nums) - n * nums[n-k].
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = sum(i * num for i, num in enumerate(nums))
        max_f = f

        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            if f > max_f:
                max_f = f

        return max_f
