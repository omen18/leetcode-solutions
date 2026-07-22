"""
Problem: Reorder Routes to Make All Paths Lead to the City Zero
LeetCode #: 1466
Difficulty: Medium
Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

Approach: Treat edges as undirected but tag direction (1 for original u->v, 0 for reversed v->u). Traverse outward from city 0; if moving along an original directed edge (away from 0), it must be reversed.
Time Complexity: O(N) where N is number of cities.
Space Complexity: O(N) for adjacency list and recursion stack.
"""

from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))  # original direction
            adj[v].append((u, 0))  # reverse direction

        visited = [False] * n
        changes = 0

        def dfs(node: int) -> None:
            nonlocal changes
            visited[node] = True
            for neighbor, direction in adj[node]:
                if not visited[neighbor]:
                    changes += direction
                    dfs(neighbor)

        dfs(0)
        return changes
