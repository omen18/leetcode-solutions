"""
Problem: Uncrossed Lines
LeetCode #: 1035
Difficulty: Medium
Link: https://leetcode.com/problems/uncrossed-lines/

Approach: Dynamic Programming (Longest Common Subsequence). Connecting matching numbers without crossing lines
is equivalent to finding the length of the Longest Common Subsequence of `nums1` and `nums2`.
Time Complexity: O(M * N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            prev = 0
            for j in range(1, n + 1):
                temp = dp[j]
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n]
