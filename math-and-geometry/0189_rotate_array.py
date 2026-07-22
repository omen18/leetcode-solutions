"""
Problem: Rotate Array
LeetCode #: 189
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-array/

Approach: In-place array reversal. Normalize k = k % n, then reverse the entire array, reverse the first k elements, and reverse the remaining n - k elements.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
