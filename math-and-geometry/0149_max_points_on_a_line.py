"""
Problem: Max Points on a Line
LeetCode #: 149
Difficulty: Hard
Link: https://leetcode.com/problems/max-points-on-a-line/

Approach: For each point, calculate simplified fractional slopes (dx/gcd, dy/gcd) to all other points and find the max count.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from collections import defaultdict
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_pts = 1

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                g = math.gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize sign for slope representation
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                slopes[(dx, dy)] += 1

            if slopes:
                max_pts = max(max_pts, max(slopes.values()) + 1)

        return max_pts
