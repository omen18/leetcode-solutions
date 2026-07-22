"""
Problem: Find Median from Data Stream
LeetCode #: 295
Difficulty: Hard
Link: https://leetcode.com/problems/find-median-from-data-stream/

Approach: Two heaps. Max-heap stores smaller half of numbers, min-heap stores larger half. Keep heaps balanced in size.
Time Complexity: O(log N) for addNum, O(1) for findMedian.
Space Complexity: O(N) to store N stream numbers in heaps.
"""

import heapq


class MedianFinder:

    def __init__(self):
        # small is max-heap (invert values), large is min-heap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # Ensure elements in small <= elements in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes (small can have at most 1 extra element)
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
