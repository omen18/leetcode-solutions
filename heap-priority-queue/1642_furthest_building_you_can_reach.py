"""
Problem: Furthest Building You Can Reach
LeetCode #: 1642
Difficulty: Medium
Link: https://leetcode.com/problems/furthest-building-you-can-reach/

Approach: Use a Min-Heap to allocate ladders for the largest height diffs.
For each jump where height diff > 0, push the climb height onto the min-heap.
If min-heap size exceeds `ladders`, pop the minimum climb and pay for it with `bricks`.
If `bricks` become negative, we cannot reach the current building, return index `i`.
If loop finishes, return the last building index `len(heights) - 1`.

Time Complexity: O(N log L) where N is number of buildings, L is number of ladders
Space Complexity: O(L)
"""

import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(min_heap, diff)
                if len(min_heap) > ladders:
                    bricks -= heapq.heappop(min_heap)
                if bricks < 0:
                    return i

        return len(heights) - 1
