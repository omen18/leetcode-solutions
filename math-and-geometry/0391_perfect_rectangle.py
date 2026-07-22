"""
Problem: Perfect Rectangle
LeetCode #: 391
Difficulty: Hard
Link: https://leetcode.com/problems/perfect-rectangle/

Approach: Verify area sum matching bounding box and check that interior corner vertices cancel out, leaving exactly the 4 outer bounding box corners.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x = float("inf")
        min_y = float("inf")
        max_x = float("-inf")
        max_y = float("-inf")

        total_area = 0
        corners = set()

        for rect in rectangles:
            x1, y1, x2, y2 = rect

            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            total_area += (x2 - x1) * (y2 - y1)

            pts = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
            for pt in pts:
                if pt in corners:
                    corners.remove(pt)
                else:
                    corners.add(pt)

        expected_area = (max_x - min_x) * (max_y - min_y)
        if total_area != expected_area:
            return False

        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y),
        }

        return corners == expected_corners
