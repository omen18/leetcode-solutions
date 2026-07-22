"""
Problem: Minimum Number of Days to Make m Bouquets
LeetCode #: 1482
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

Approach: Binary search on days in range [min(bloomDay), max(bloomDay)]. For a day d, count consecutive flowers bloomed (<= d) to form bouquets of size k.
Time Complexity: O(n * log(max(bloomDay)))
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            bouquets = 0
            flowers = 0

            for day in bloomDay:
                if day <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                right = mid
            else:
                left = mid + 1

        return left
