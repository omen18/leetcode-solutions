"""
Problem: Longest Increasing Subsequence
LeetCode #: 300
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Approach: Patience sorting with binary search (bisect_left) to maintain tail values of active subsequences.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
