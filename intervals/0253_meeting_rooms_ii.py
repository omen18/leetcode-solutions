"""
Problem: Meeting Rooms II
LeetCode #: 253
Difficulty: Medium
Link: https://leetcode.com/problems/meeting-rooms-ii/

Approach: Sort intervals by start time. Use a min-heap to keep track of end times of active meetings.
Time Complexity: O(N log N)
Space Complexity: O(N) for min-heap
"""

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        free_rooms = []  # Min-heap storing end times

        heapq.heappush(free_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if free_rooms[0] <= interval[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, interval[1])

        return len(free_rooms)
