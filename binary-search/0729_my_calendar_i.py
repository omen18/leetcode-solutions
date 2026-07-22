"""
Problem: My Calendar I
LeetCode #: 729
Difficulty: Medium
Link: https://leetcode.com/problems/my-calendar-i/

Approach: Maintain a sorted list of booked intervals `(start, end)`. Use binary search (bisect_right) to insert interval and check if it overlaps with adjacent intervals.
Time Complexity: O(n log n) per booking due to bisect (O(log n)) and insertion (O(n))
Space Complexity: O(n)
"""

import bisect


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.calendar, (start, end))

        # Check overlap with previous event
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False

        # Check overlap with next event
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False

        self.calendar.insert(idx, (start, end))
        return True
