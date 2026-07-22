"""
Problem: Network Delay Time
LeetCode #: 743
Difficulty: Medium
Link: https://leetcode.com/problems/network-delay-time/

Approach: Dijkstra's algorithm using a min-heap to compute the shortest paths from source node k to all other nodes. Return max distance if all nodes visited, else -1.
Time Complexity: O(E log V) where E is length of times and V is n.
Space Complexity: O(V + E) for graph storage and heap.
"""

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        pq = [(0, k)]
        dist = {}

        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for neighbor, weight in adj[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (d + weight, neighbor))

        return max(dist.values()) if len(dist) == n else -1
