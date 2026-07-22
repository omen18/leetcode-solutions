"""
Problem: Water and Jug Problem
LeetCode #: 365
Difficulty: Medium
Link: https://leetcode.com/problems/water-and-jug-problem/

Approach: Mathematical solution using Bézout's Identity and Greatest Common Divisor (GCD).
Time Complexity: O(log(min(x, y)))
Space Complexity: O(1)
"""

import math


class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        if target == 0:
            return True
        return target % math.gcd(x, y) == 0
