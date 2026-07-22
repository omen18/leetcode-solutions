"""
Problem: Merge Intervals
LeetCode #: 56
Difficulty: Medium
Link: https://leetcode.com/problems/merge-intervals/

Approach: Sort intervals by start time. Iterate and merge overlapping intervals if current start <= previous end.
Time Complexity: O(N log N) sorting
Space Complexity: O(N) for output array
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
