"""
Problem: Minimum Height Trees
LeetCode #: 310
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-height-trees/

Approach: Topological trim (BFS leaf stripping). A tree can have at most two centroids (roots of minimum height trees). Iteratively remove leaves (nodes with degree 1) layer by layer until 1 or 2 nodes remain.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = deque([i for i in range(n) if len(adj[i]) == 1])

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)
