"""
Problem: K Closest Points to Origin
LeetCode #: 973
Difficulty: Medium
Link: https://leetcode.com/problems/k-closest-points-to-origin/

Approach: Maintain a Max-Heap of size k storing (-dist_sq, x, y).
For each point, calculate distance squared x^2 + y^2. Push (-dist_sq, x, y) onto heap.
If heap size exceeds k, pop the maximum distance point.
At the end, extract all remaining points from the heap.

Time Complexity: O(N log k)
Space Complexity: O(k)
"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = -(x * x + y * y)
            heapq.heappush(max_heap, (dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for _, x, y in max_heap]
