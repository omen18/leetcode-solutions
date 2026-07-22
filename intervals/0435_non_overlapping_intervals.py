"""
Problem: Non-overlapping Intervals
LeetCode #: 435
Difficulty: Medium
Link: https://leetcode.com/problems/non-overlapping-intervals/

Approach: Greedy approach sorting intervals by end time. Always pick the interval that finishes earliest to leave max room for remaining.
Time Complexity: O(N log N)
Space Complexity: O(1) auxiliary
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1
            else:
                prev_end = intervals[i][1]

        return count
