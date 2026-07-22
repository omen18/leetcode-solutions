"""
Problem: Binary Subarrays With Sum
LeetCode #: 930
Difficulty: Medium
Link: https://leetcode.com/problems/binary-subarrays-with-sum/

Approach: Number of subarrays with exact sum `goal` equals `atMost(goal) - atMost(goal - 1)` using sliding window.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(k: int) -> int:
            if k < 0:
                return 0
            left = 0
            current_sum = 0
            count = 0
            for right in range(len(nums)):
                current_sum += nums[right]
                while current_sum > k:
                    current_sum -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        return atMost(goal) - atMost(goal - 1)
