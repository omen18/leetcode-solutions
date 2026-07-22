"""
Problem: Max Consecutive Ones III
LeetCode #: 1004
Difficulty: Medium
Link: https://leetcode.com/problems/max-consecutive-ones-iii/

Approach: Sliding window allowing at most `k` zeros. Increment zero count on encountering 0; shrink from left when zero count > k.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
