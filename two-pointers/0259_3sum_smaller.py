"""
Problem: 3Sum Smaller
LeetCode #: 259
Difficulty: Medium
Link: https://leetcode.com/problems/3sum-smaller/

Approach: Sorting + Two Pointers. Sort `nums`. For each element i, use two pointers `left = i + 1` and `right = len(nums) - 1`. If `nums[i] + nums[left] + nums[right] < target`, then all indices between `left` and `right` pair with `left` to form valid triplets, so add `right - left` to count and increment `left`. Otherwise, decrement `right`.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count
