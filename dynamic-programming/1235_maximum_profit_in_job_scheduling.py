"""
Problem: Maximum Profit in Job Scheduling
LeetCode #: 1235
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/

Approach: Dynamic Programming with Binary Search.
Sort jobs by their end times. Maintain `dp[i]` storing the maximum profit using a subset of the first `i` jobs.
For job `i` `(start, end, profit)`, use `bisect_right` on end times to find the latest non-overlapping job `idx`.
`dp[i] = max(dp[i - 1], profit + dp[idx])`.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

import bisect
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [j[1] for j in jobs]
        n = len(jobs)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            start, end, p = jobs[i - 1]
            # Find the latest job that finishes <= current job's start time
            idx = bisect.bisect_right(end_times, start, 0, i - 1)
            dp[i] = max(dp[i - 1], p + dp[idx])

        return dp[n]
