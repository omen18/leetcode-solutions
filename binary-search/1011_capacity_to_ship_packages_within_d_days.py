"""
Problem: Capacity To Ship Packages Within D Days
LeetCode #: 1011
Difficulty: Medium
Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Approach: Binary search on capacity range [max(weights), sum(weights)]. For a given capacity, simulate greedy loading and count required days.
Time Complexity: O(n * log(sum(weights) - max(weights)))
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            current_weight = 0
            required_days = 1

            for w in weights:
                if current_weight + w > mid:
                    required_days += 1
                    current_weight = 0
                current_weight += w

            if required_days <= days:
                right = mid
            else:
                left = mid + 1

        return left
