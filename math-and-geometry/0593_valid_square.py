"""
Problem: Valid Square
LeetCode #: 593
Difficulty: Medium
Link: https://leetcode.com/problems/valid-square/

Approach: Calculate squared distances between all pair combinations. A valid square has exactly 2 distinct non-zero distances (4 sides, 2 diagonals).
Time Complexity: O(1)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def dist_sq(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        pts = [p1, p2, p3, p4]
        distances = set()

        for i in range(4):
            for j in range(i + 1, 4):
                d = dist_sq(pts[i], pts[j])
                if d == 0:
                    return False
                distances.add(d)

        return len(distances) == 2
