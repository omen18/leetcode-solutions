"""
Problem: Longest Subarray of 1's After Deleting One Element
LeetCode #: 1493
Difficulty: Medium
Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Approach: Find longest window containing at most 1 zero (k=1). The answer is window size minus 1 (since we must delete one element).
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left)

        return max_len
