"""
Problem: Maximum Number of Events That Can Be Attended
LeetCode #: 1353
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

Approach: Sort events by start day. Use a min-heap to keep track of end days of available events.
Iterate day by day from 1 to the maximum end day of all events.
Add end days of all events starting on the current day to the min-heap.
Remove events from min-heap that have already ended (end < day).
Pop the event with the earliest end day from min-heap, attend it, and increment count.

Time Complexity: O(N log N + D log N) where N is number of events and D is max end day
Space Complexity: O(N)
"""

import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        min_heap = []
        i, n = 0, len(events)
        res = 0
        day = 0

        while i < n or min_heap:
            if not min_heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                res += 1
                day += 1

        return res
