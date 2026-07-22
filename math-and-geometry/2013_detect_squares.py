"""
Problem: Detect Squares
LeetCode #: 2013
Difficulty: Medium
Link: https://leetcode.com/problems/detect-squares/

Approach: Maintain point frequencies in a hash map. For each query point, iterate through points that form a diagonal of a square with non-zero side length.
Time Complexity: O(1) for add, O(N) for count where N is the number of unique added points.
Space Complexity: O(N)
"""

from collections import Counter
from typing import List


class DetectSquares:
    def __init__(self):
        self.pts_count = Counter()
        self.pts_by_x = Counter()  # x -> list of y's or counter of y's

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts_count[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        total_squares = 0

        # Look for potential diagonal opposite points (x, y)
        for (x, y), freq in self.pts_count.items():
            if abs(x - px) == abs(y - py) and x != px:
                # The other two required corners are (px, y) and (x, py)
                c1 = self.pts_count[(px, y)]
                c2 = self.pts_count[(x, py)]
                total_squares += freq * c1 * c2

        return total_squares
