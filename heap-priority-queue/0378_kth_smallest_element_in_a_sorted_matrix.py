"""
Problem: Kth Smallest Element in a Sorted Matrix
LeetCode #: 378
Difficulty: Medium
Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Approach: Store (matrix[r][c], r, c) in a min-heap initialized with the first element of each row r < min(N, k).
Pop the min element k times. Whenever an element (val, r, c) is popped, push the next element in the same row (matrix[r][c+1], r, c+1) if c+1 < N.

Time Complexity: O(k log min(N, k)) where N is matrix size
Space Complexity: O(min(N, k))
"""

import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        for r in range(min(n, k)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        val = 0
        for _ in range(k):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return val
