"""
Problem: Employee Free Time
LeetCode #: 759
Difficulty: Hard
Link: https://leetcode.com/problems/employee-free-time/

Approach: Flatten and sort all working intervals by start time. Merge overlapping working intervals; gaps between merged intervals represent free time.
Time Complexity: O(N log N) where N is total number of intervals across all employees
Space Complexity: O(N)
"""

from typing import List


class Interval:
    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for emp in schedule:
            for iv in emp:
                intervals.append(iv)

        intervals.sort(key=lambda x: x.start)

        res = []
        prev_end = intervals[0].end

        for iv in intervals[1:]:
            if iv.start > prev_end:
                res.append(Interval(prev_end, iv.start))
                prev_end = iv.end
            else:
                prev_end = max(prev_end, iv.end)

        return res
