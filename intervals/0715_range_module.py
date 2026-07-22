"""
Problem: Range Module
LeetCode #: 715
Difficulty: Hard
Link: https://leetcode.com/problems/range-module/

Approach: Maintain disjoint sorted list of interval endpoints [left, right). Use binary search (bisect) for queries and range updates.
Time Complexity: addRange/removeRange: O(N), queryRange: O(log N)
Space Complexity: O(N) for storing non-overlapping intervals
"""

import bisect


class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)

        sub = []
        if i % 2 == 0:
            sub.append(left)
        if j % 2 == 0:
            sub.append(right)

        self.track[i:j] = sub

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.track, left)
        j = bisect.bisect_left(self.track, right)
        return i == j and i % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.track, left)
        j = bisect.bisect_right(self.track, right)

        sub = []
        if i % 2 == 1:
            sub.append(left)
        if j % 2 == 1:
            sub.append(right)

        self.track[i:j] = sub
