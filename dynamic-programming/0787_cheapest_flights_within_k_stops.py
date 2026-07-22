"""
Problem: Cheapest Flights Within K Stops
LeetCode #: 787
Difficulty: Medium
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Approach: Dynamic Programming / Bellman-Ford algorithm. Maintain a distance array of size N initialized to infinity,
with `dist[src] = 0`. Perform K + 1 iterations. In each iteration, update distances based on edge relaxation from
the previous iteration state to avoid using more than K stops in a single step.
Time Complexity: O(K * E) where E is number of flights
Space Complexity: O(V) where V is number of cities
"""

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = list(dist)
            for u, v, w in flights:
                if dist[u] != float('inf') and dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w
            dist = temp

        return int(dist[dst]) if dist[dst] != float('inf') else -1
