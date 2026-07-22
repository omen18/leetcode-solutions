"""
Problem: Total Cost to Hire K Workers
LeetCode #: 2462
Difficulty: Medium
Link: https://leetcode.com/problems/total-cost-to-hire-k-workers/

Approach: Maintain two min-heaps. `left_heap` contains workers from the left side, `right_heap` from the right side.
In each of k sessions, pick the minimum cost worker between top of left_heap and right_heap.
If costs are equal, break tie by picking from left_heap. Refill heap from corresponding side if left pointer <= right pointer.

Time Complexity: O(k log candidates + candidates log candidates)
Space Complexity: O(candidates)
"""

import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l = 0
        r = len(costs) - 1

        left_heap = []
        right_heap = []

        while l <= r and len(left_heap) < candidates:
            heapq.heappush(left_heap, costs[l])
            l += 1

        while l <= r and len(right_heap) < candidates:
            heapq.heappush(right_heap, costs[r])
            r -= 1

        total = 0

        for _ in range(k):
            val1 = left_heap[0] if left_heap else float('inf')
            val2 = right_heap[0] if right_heap else float('inf')

            if val1 <= val2:
                total += heapq.heappop(left_heap)
                if l <= r:
                    heapq.heappush(left_heap, costs[l])
                    l += 1
            else:
                total += heapq.heappop(right_heap)
                if l <= r:
                    heapq.heappush(right_heap, costs[r])
                    r -= 1

        return total
