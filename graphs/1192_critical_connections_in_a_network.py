"""
Problem: Critical Connections in a Network
LeetCode #: 1192
Difficulty: Hard
Link: https://leetcode.com/problems/critical-connections-in-a-network/

Approach: Tarjan's Bridge Detection Algorithm.
Track discovery time `disc` and lowest reachable rank `low` during DFS.
An edge (u, v) is a critical connection if `low[v] > disc[u]`, meaning node `v` cannot reach `u` or any ancestor of `u` without using edge (u, v).

Time Complexity: O(V + E) where V = n and E = len(connections).
Space Complexity: O(V + E) for graph storage and recursion depth.
"""

from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1] * n
        low = [-1] * n
        bridges = []
        timer = 0

        def dfs(node: int, parent: int) -> None:
            nonlocal timer
            disc[node] = low[node] = timer
            timer += 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                if disc[neighbor] != -1:
                    low[node] = min(low[node], disc[neighbor])
                else:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        bridges.append([node, neighbor])

        dfs(0, -1)
        return bridges
