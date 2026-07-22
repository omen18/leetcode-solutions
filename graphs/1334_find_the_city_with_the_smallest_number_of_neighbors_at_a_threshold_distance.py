"""
Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance
LeetCode #: 1334
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

Approach: Floyd-Warshall Algorithm for all-pairs shortest paths.
Compute the shortest path matrix dist[u][v]. Count how many cities each city can reach
within `distanceThreshold`. Return the city with the minimal count, choosing the highest-indexed city on ties.

Time Complexity: O(N^3) where N is number of cities.
Space Complexity: O(N^2) for the distance matrix.
"""

from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        inf = float("inf")
        dist = [[inf] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        min_reachable = n
        result_city = -1

        for i in range(n):
            reachable = sum(
                1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold
            )
            if reachable <= min_reachable:
                min_reachable = reachable
                result_city = i

        return result_city
