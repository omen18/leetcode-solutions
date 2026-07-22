"""
Problem: Insert Interval
LeetCode #: 57
Difficulty: Medium
Link: https://leetcode.com/problems/insert-interval/

Approach: Add non-overlapping intervals before newInterval, merge all overlapping ones with newInterval, then add non-overlapping ones after.
Time Complexity: O(N) linear scan
Space Complexity: O(N) output
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
