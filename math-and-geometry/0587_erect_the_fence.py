"""
Problem: Erect the Fence
LeetCode #: 587
Difficulty: Hard
Link: https://leetcode.com/problems/erect-the-fence/

Approach: Monotone Chain Convex Hull algorithm modified to include collinear points on the perimeter boundary.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross_product(p1, p2, p3):
            return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (
                p3[0] - p1[0]
            )

        trees.sort(key=lambda p: (p[0], p[1]))

        # Build lower hull
        lower = []
        for p in trees:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Remove duplicate points
        hull = set(tuple(p) for p in lower + upper)
        return [list(p) for p in hull]
