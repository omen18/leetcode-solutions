"""
Problem: Count Subarrays With Fixed Bounds
LeetCode #: 2444
Difficulty: Hard
Link: https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

Approach: One pass sliding window. Track latest indices `bad_idx` (out of range element), `min_idx` (element equal to minK), and `max_idx` (element equal to maxK). Valid subarrays ending at `i` start between `bad_idx + 1` and `min(min_idx, max_idx)`.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        bad_idx = -1
        min_idx = -1
        max_idx = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_idx = i
            if num == minK:
                min_idx = i
            if num == maxK:
                max_idx = i

            valid_starts = min(min_idx, max_idx) - bad_idx
            if valid_starts > 0:
                ans += valid_starts

        return ans
