"""
Problem: Koko Eating Bananas
LeetCode #: 875
Difficulty: Medium
Link: https://leetcode.com/problems/koko-eating-bananas/

Approach: Binary search on eating speed k within range [1, max(piles)]. For a speed k, calculate total hours required and check if <= h.
Time Complexity: O(n * log(max(piles)))
Space Complexity: O(1)
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)

            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
