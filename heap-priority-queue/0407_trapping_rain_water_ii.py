"""
Problem: Trapping Rain Water II
LeetCode #: 407
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water-ii/

Approach: Use a Min-Heap and visited matrix starting from boundary cells.
Push all outer boundary cells into the min-heap storing (height, r, c) and mark them visited.
Repeatedly pop cell with smallest height `(h, r, c)` from heap.
For each unvisited 4-directional neighbor `(nr, nc)`, trapped water is `max(0, h - heightMap[nr][nc])`.
Push neighbor onto min-heap with updated effective boundary height `max(h, heightMap[nr][nc])` and mark visited.

Time Complexity: O(M * N log(M * N))
Space Complexity: O(M * N)
"""

import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []

        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        trapped_water = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:
            h, r, c = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    trapped_water += max(0, h - heightMap[nr][nc])
                    heapq.heappush(min_heap, (max(h, heightMap[nr][nc]), nr, nc))

        return trapped_water
