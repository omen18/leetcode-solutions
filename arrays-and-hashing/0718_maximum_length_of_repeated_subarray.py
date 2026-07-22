"""
Problem: Maximum Length of Repeated Subarray
LeetCode #: 718
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-length-of-repeated-subarray/

Approach: 2D dynamic programming storing max subarray suffix length at dp[i][j] for nums1[i-1] == nums2[j-1].
Time Complexity: O(M * N) where M, N are lengths of nums1 and nums2.
Space Complexity: O(M * N) for 2D DP array.
"""

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len
