"""
Problem: Minimum Swaps To Make Sequences Increasing
LeetCode #: 801
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

Approach: Dynamic Programming with state compression. Maintain `keep` (min swaps up to index i-1 without swapping at i-1)
and `swap` (min swaps up to index i-1 with swapping at i-1). For index i, evaluate conditions for keeping and swapping.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        keep = 0
        swap = 1

        for i in range(1, n):
            new_keep = float('inf')
            new_swap = float('inf')

            # Case 1: Elements already in order without swap at current step relative to previous state
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                new_keep = min(new_keep, keep)
                new_swap = min(new_swap, swap + 1)

            # Case 2: Elements in order if we swap one and keep the other
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                new_keep = min(new_keep, swap)
                new_swap = min(new_swap, keep + 1)

            keep, swap = new_keep, new_swap

        return min(keep, swap)
