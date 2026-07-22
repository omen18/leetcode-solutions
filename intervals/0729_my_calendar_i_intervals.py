"""
Problem: My Calendar I
LeetCode #: 729
Difficulty: Medium
Link: https://leetcode.com/problems/my-calendar-i/

Approach: Binary search (bisect) maintaining sorted intervals [start, end) without overlaps.
Time Complexity: O(N log N) total or O(N) insertion, binary search O(log N)
Space Complexity: O(N) to store bookings
"""

import bisect


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.calendar, (start, end))

        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False

        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False

        self.calendar.insert(idx, (start, end))
        return True
