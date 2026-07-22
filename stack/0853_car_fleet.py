"""
Problem: Car Fleet
LeetCode #: 853
Difficulty: Medium
Link: https://leetcode.com/problems/car-fleet/

Approach:
Sort cars by starting position in descending order (closest to target first).
Calculate time required for each car to reach target: `(target - position) / speed`.
Iterate through sorted cars and maintain a stack of fleet arrival times.
If a car behind has arrival time <= car in front (stack top), it catches up and joins the fleet ahead.
Otherwise, it forms a new fleet and its arrival time is pushed onto stack.

Time Complexity: O(N log N) due to sorting, where N is the number of cars.
Space Complexity: O(N) to store car pairs and stack.
"""

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pair:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
