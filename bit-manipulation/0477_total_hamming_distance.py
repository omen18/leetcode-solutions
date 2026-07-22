"""
Problem: Total Hamming Distance
LeetCode #: 477
Difficulty: Medium
Link: https://leetcode.com/problems/total-hamming-distance/

Approach: For each of the 32 bit positions, count set bits k. Total distance contribution is k * (N - k).
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total_distance = 0

        for bit in range(32):
            ones = sum((num >> bit) & 1 for num in nums)
            total_distance += ones * (n - ones)

        return total_distance
