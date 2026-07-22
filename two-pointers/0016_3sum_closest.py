"""
Problem: 3Sum Closest
LeetCode #: 16
Difficulty: Medium
Link: https://leetcode.com/problems/3sum-closest/

Approach: Sort array, iterate through each element `i` and use two pointers for remaining array. Track triplet sum closest to target.
Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target

        return closest_sum
