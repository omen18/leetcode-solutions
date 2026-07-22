"""
Problem: Design Underground System
LeetCode #: 1396
Difficulty: Medium
Link: https://leetcode.com/problems/design-underground-system/

Approach: Use two hash maps: one to store customer check-ins (id -> start_station, check_in_time) and another to aggregate trip statistics ((start_station, end_station) -> total_time, count).
Time Complexity: O(1) for checkIn, checkOut, and getAverageTime operations.
Space Complexity: O(P + U) where P is the number of station pairs and U is active check-ins.
"""

from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_ins = {}  # id -> (stationName, t)
        self.travel_times = defaultdict(lambda: [0, 0])  # (start, end) -> [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins.pop(id)
        duration = t - check_in_time
        pair = (start_station, stationName)
        self.travel_times[pair][0] += duration
        self.travel_times[pair][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times[(startStation, endStation)]
        return total_time / count
