"""
Problem: Number of Pairs of Interchangeable Rectangles
LeetCode #: 2001
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

Approach: Calculate simplified width/height ratio using GCD for precision and count occurrences in hash map.
Time Complexity: O(N * log(min(w, h))) where N is number of rectangles.
Space Complexity: O(N) for ratio frequency map.
"""

from collections import defaultdict
import math
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = defaultdict(int)

        for w, h in rectangles:
            g = math.gcd(w, h)
            ratio = (w // g, h // g)
            ratio_count[ratio] += 1

        ans = 0
        for count in ratio_count.values():
            ans += count * (count - 1) // 2

        return ans
