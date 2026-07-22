"""
Problem: Min Cost to Connect All Points
LeetCode #: 1584
Difficulty: Medium
Link: https://leetcode.com/problems/min-cost-to-connect-all-points/

Approach: Compute Minimum Spanning Tree (MST) using Prim's algorithm with a min-heap. Distance between points (x1, y1) and (x2, y2) is Manhattan distance |x1 - x2| + |y1 - y2|.
Time Complexity: O(N^2 log N) where N is the number of points.
Space Complexity: O(N^2) for heap and visited set.
"""

from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, node)
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            total_cost += cost
            x1, y1 = points[u]

            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, v))

        return total_cost
