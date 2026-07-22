"""
Problem: Minimum Number of Arrows to Burst Balloons
LeetCode #: 452
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Approach: Sort balloons by end coordinates. Place arrows at the end of overlapping intervals to maximize balloons burst per arrow.
Time Complexity: O(N log N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
            
        points.sort(key=lambda x: x[1])
        arrows = 1
        prev_end = points[0][1]
        
        for start, end in points[1:]:
            if start > prev_end:
                arrows += 1
                prev_end = end
                
        return arrows
