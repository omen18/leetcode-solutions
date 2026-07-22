"""
Problem: Divide Intervals Into Minimum Number of Groups
LeetCode #: 2406
Difficulty: Medium
Link: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

Approach: Min-heap to track smallest right endpoint of active groups, similar to Meeting Rooms II.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []

        for start, end in intervals:
            if heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
