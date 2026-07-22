"""
Problem: Keys and Rooms
LeetCode #: 841
Difficulty: Medium
Link: https://leetcode.com/problems/keys-and-rooms/

Approach: Breadth-First Search (BFS) or DFS to visit rooms starting with room 0. Collect keys found in visited rooms to unlock next rooms. Check if all rooms are visited.
Time Complexity: O(V + E) where V is number of rooms and E total keys.
Space Complexity: O(V) for visited set and queue.
"""

from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        queue = deque([0])

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)
