"""
Problem: IPO
LeetCode #: 502
Difficulty: Hard
Link: https://leetcode.com/problems/ipo/

Approach: Pair projects by (capital, profit) and sort by capital required.
Maintain a Max-Heap for available profits of affordable projects.
Iterate k times:
  - Push all available projects with required capital <= current capital `w` into max-heap.
  - If max-heap is empty, no further project can be undertaken, break early.
  - Pop project with highest profit, add profit to capital `w`.

Time Complexity: O(N log N + k log N)
Space Complexity: O(N)
"""

import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w
