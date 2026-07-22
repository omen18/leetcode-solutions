"""
Problem: Path With Minimum Effort
LeetCode #: 1631
Difficulty: Medium
Link: https://leetcode.com/problems/path-with-minimum-effort/

Approach: Modified Dijkstra's Algorithm using a min-heap. Maintain distance matrix where distance represents the minimum possible max-effort required to reach cell (r, c) from (0, 0).
Time Complexity: O(M * N log(M * N)) where M and N are grid dimensions.
Space Complexity: O(M * N) for effort array and min-heap.
"""

from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        pq = [(0, 0, 0)]  # (effort, r, c)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            effort, r, c = heapq.heappop(pq)

            if r == rows - 1 and c == cols - 1:
                return effort

            if effort > efforts[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(pq, (next_effort, nr, nc))

        return 0
