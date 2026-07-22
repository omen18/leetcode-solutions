"""
Problem: Find the Smallest Divisor Given a Threshold
LeetCode #: 1283
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Approach: Binary search for divisor in range [1, max(nums)]. For divisor `d`, compute sum of ceil(num / d) and compare with threshold.
Time Complexity: O(n * log(max(nums)))
Space Complexity: O(1)
"""

import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            total_sum = sum(math.ceil(num / mid) for num in nums)

            if total_sum <= threshold:
                right = mid
            else:
                left = mid + 1

        return left
