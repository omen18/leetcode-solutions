"""
Problem: Remove Covered Intervals
LeetCode #: 1288
Difficulty: Medium
Link: https://leetcode.com/problems/remove-covered-intervals/

Approach: Sort intervals by start ascending, end descending. Iterate and keep track of max end seen so far.
Time Complexity: O(N log N)
Space Complexity: O(1) auxiliary
"""

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        prev_end = 0

        for interval in intervals:
            if interval[1] > prev_end:
                count += 1
                prev_end = interval[1]

        return count
