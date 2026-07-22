"""
Problem: Increasing Triplet Subsequence
LeetCode #: 334
Difficulty: Medium
Link: https://leetcode.com/problems/increasing-triplet-subsequence/

Approach: Maintain two variables `first` and `second` representing the smallest and second smallest values seen so far. If a number strictly greater than `second` is encountered, an increasing triplet exists.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
