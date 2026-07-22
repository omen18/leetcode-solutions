"""
Problem: Generate Random Point in a Circle
LeetCode #: 478
Difficulty: Medium
Link: https://leetcode.com/problems/generate-random-point-in-a-circle/

Approach: Polar coordinates with sqrt transformation for uniform area sampling.
Time Complexity: O(1) per point generation
Space Complexity: O(1)
"""

import math
import random
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Uniform sampling in circle requires r = R * sqrt(u)
        r = self.radius * math.sqrt(random.uniform(0, 1))
        theta = random.uniform(0, 2 * math.pi)
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)
        return [x, y]
