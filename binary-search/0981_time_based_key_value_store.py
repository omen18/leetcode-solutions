"""
Problem: Time Based Key-Value Store
LeetCode #: 981
Difficulty: Medium
Link: https://leetcode.com/problems/time-based-key-value-store/

Approach: Store values in a hash map of lists containing (timestamp, value) pairs. Since timestamps are strictly increasing, use binary search (bisect_right) to find the largest timestamp <= requested timestamp.
Time Complexity: set: O(1), get: O(log k) where k is the number of values for the key
Space Complexity: O(N) total stored entries
"""

import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        pairs = self.store[key]
        idx = bisect.bisect_right(pairs, (timestamp, chr(127))) - 1

        if idx >= 0:
            return pairs[idx][1]
        return ""
