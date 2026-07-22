"""
Problem: Last Stone Weight
LeetCode #: 1046
Difficulty: Easy
Link: https://leetcode.com/problems/last-stone-weight/

Approach: Put all stone weights into a max-heap (by negating values).
Repeatedly pop the two heaviest stones y and x (y >= x).
If y != x, push (y - x) back into the max-heap.
Repeat until at most 1 stone remains.

Time Complexity: O(N log N)
Space Complexity: O(N)
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if y != x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0
