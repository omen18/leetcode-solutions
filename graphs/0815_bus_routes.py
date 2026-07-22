"""
Problem: Bus Routes
LeetCode #: 815
Difficulty: Hard
Link: https://leetcode.com/problems/bus-routes/

Approach: BFS on Route Graph.
Build a map from each stop to its set of bus route indices.
Perform BFS where states represent bus routes rather than individual stops.
Enqueue initial routes serving `source`, and traverse shared stops to discover connected routes until `target` is reached.

Time Complexity: O(N * S) where N is number of routes and S is maximum number of stops per route.
Space Complexity: O(N * S) for stop-to-route map and BFS structures.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)

        queue = deque()
        visited_routes = set()

        for route_idx in stop_to_routes[source]:
            queue.append((route_idx, 1))
            visited_routes.add(route_idx)

        visited_stops = {source}

        while queue:
            curr_route, buses = queue.popleft()

            for stop in routes[curr_route]:
                if stop == target:
                    return buses

                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            visited_routes.add(next_route)
                            queue.append((next_route, buses + 1))

        return -1
