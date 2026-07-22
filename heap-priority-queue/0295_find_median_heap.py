"""
Problem: Find Median from Data Stream
LeetCode #: 295
Difficulty: Hard
Link: https://leetcode.com/problems/find-median-from-data-stream/

Approach: Maintain two heaps:
  - `small`: Max-heap storing the smaller half of the numbers (negated values in Python).
  - `large`: Min-heap storing the larger half of the numbers.
For each added number, push to `small` max-heap first, then move the maximum element of `small` to `large`.
If `large` has more elements than `small`, move top of `large` to `small` to maintain size invariant: len(small) == len(large) or len(small) == len(large) + 1.
Median is top of `small` (if odd total count) or average of top of `small` and top of `large` (if even).

Time Complexity:
  - addNum: O(log N)
  - findMedian: O(1)
Space Complexity: O(N)
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (store negated values)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
