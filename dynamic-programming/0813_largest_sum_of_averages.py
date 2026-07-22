"""
Problem: Largest Sum of Averages
LeetCode #: 813
Difficulty: Medium
Link: https://leetcode.com/problems/largest-sum-of-averages/

Approach: Dynamic Programming. Compute prefix sums for O(1) subarray sum calculation. `dp[i]` represents max average sum
to partition `nums[:i]` into `m` groups. For each group count `m` from 2 to `k`, update `dp[i]` as
`max(dp[j] + average(j..i-1))` for `j < i`.
Time Complexity: O(K * N^2)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def average(i: int, j: int) -> float:
            return (prefix[j] - prefix[i]) / (j - i)

        # Base case: 1 partition
        dp = [average(0, i) for i in range(1, n + 1)]

        # k partitions
        for _ in range(2, k + 1):
            next_dp = [0.0] * n
            for i in range(n):
                for j in range(i):
                    next_dp[i] = max(next_dp[i], dp[j] + average(j + 1, i + 1))
            dp = next_dp

        return dp[-1]
