"""
Problem: Minimum Number of Arrows to Burst Balloons
LeetCode #: 452
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Approach: Greedy approach sorting balloons by end coordinate. Shoot arrow at end coordinate of current balloon.
Time Complexity: O(N log N)
Space Complexity: O(1) auxiliary
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        prev_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > prev_end:
                arrows += 1
                prev_end = points[i][1]

        return arrows
