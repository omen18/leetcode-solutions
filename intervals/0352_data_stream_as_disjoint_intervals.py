"""
Problem: Data Stream as Disjoint Intervals
LeetCode #: 352
Difficulty: Hard
Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/

Approach: Maintain disjoint merged intervals in sorted order using binary search (bisect_left) upon inserting each new value.
Time Complexity: O(N) per addNum for insertion into list (or O(log N) search), O(1) or O(N) for getIntervals
Space Complexity: O(N) to store intervals
"""

import bisect
from typing import List


class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        idx = bisect.bisect_left(self.intervals, [value, value])

        if idx > 0 and self.intervals[idx - 1][1] >= value:
            return

        left_merge = (idx > 0 and self.intervals[idx - 1][1] + 1 == value)
        right_merge = (idx < len(self.intervals) and self.intervals[idx][0] - 1 == value)

        if left_merge and right_merge:
            self.intervals[idx - 1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif left_merge:
            self.intervals[idx - 1][1] = value
        elif right_merge:
            self.intervals[idx][0] = value
        else:
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
