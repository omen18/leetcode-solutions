"""
Problem: Longest Arithmetic Subsequence
LeetCode #: 1027
Difficulty: Medium
Link: https://leetcode.com/problems/longest-arithmetic-subsequence/

Approach: Dynamic Programming with Hash Map. `dp[i][diff]` represents the length of the longest
arithmetic subsequence ending at index `i` with common difference `diff`. For each pair `(j, i)` with `j < i`,
calculate `diff = nums[i] - nums[j]` and update `dp[i][diff] = dp[j].get(diff, 1) + 1`.
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        max_len = 2

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i, diff] = dp.get((j, diff), 1) + 1
                max_len = max(max_len, dp[i, diff])

        return max_len
