"""
Problem: Reconstruct Itinerary
LeetCode #: 332
Difficulty: Hard
Link: https://leetcode.com/problems/reconstruct-itinerary/

Approach: Hierholzer's Algorithm for Eulerian Path.
Build adjacency graph with destinations sorted in reverse alphabetical order for efficient popping.
Use DFS post-order traversal: push node to itinerary when all outgoing edges are exhausted, then reverse result.

Time Complexity: O(E log E) where E is number of tickets.
Space Complexity: O(E) for graph adjacencies and stack recursion.
"""

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        for src in adj:
            adj[src].sort(reverse=True)

        itinerary = []

        def dfs(airport: str) -> None:
            while adj[airport]:
                next_dest = adj[airport].pop()
                dfs(next_dest)
            itinerary.append(airport)

        dfs("JFK")
        return itinerary[::-1]
