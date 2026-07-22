"""
Problem: My Calendar II
LeetCode #: 731
Difficulty: Medium
Link: https://leetcode.com/problems/my-calendar-ii/

Approach: Track single bookings and double bookings. When adding a new booking, check against double bookings for triple booking overlap.
Time Complexity: O(N^2) where N is number of bookings
Space Complexity: O(N)
"""


class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for o_start, o_end in self.overlaps:
            if max(start, o_start) < min(end, o_end):
                return False

        for b_start, b_end in self.bookings:
            if max(start, b_start) < min(end, b_end):
                self.overlaps.append((max(start, b_start), min(end, b_end)))

        self.bookings.append((start, end))
        return True
