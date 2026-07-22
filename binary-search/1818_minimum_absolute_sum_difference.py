"""
Problem: Minimum Absolute Sum Difference
LeetCode #: 1818
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-absolute-sum-difference/

Approach: Compute initial absolute sum diff. Sort a copy of nums1. For each position i, use binary search (bisect_left) on sorted nums1 to find element closest to nums2[i], keeping track of maximum difference reduction.
Time Complexity: O(n log n)
Space Complexity: O(n) for sorted copy of nums1
"""

import bisect
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)

        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_diff = sum(diffs)

        sorted_nums1 = sorted(nums1)
        max_gain = 0

        for i in range(n):
            original_diff = diffs[i]
            target = nums2[i]

            idx = bisect.bisect_left(sorted_nums1, target)

            # Check candidate at idx
            if idx < n:
                gain = original_diff - abs(sorted_nums1[idx] - target)
                max_gain = max(max_gain, gain)

            # Check candidate at idx - 1
            if idx > 0:
                gain = original_diff - abs(sorted_nums1[idx - 1] - target)
                max_gain = max(max_gain, gain)

        return (total_diff - max_gain) % MOD
