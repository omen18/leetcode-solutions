"""
Problem: Count Unreachable Pairs of Nodes in an Undirected Graph
LeetCode #: 2316
Difficulty: Medium
Link: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

Approach: Connected Components via DFS.
Find the size of each connected component in the graph. As we discover each component of size `s`,
the number of unreachable pairs contributed by this component to remaining nodes is `s * (n - s)`.

Time Complexity: O(V + E) where V = n and E = len(edges).
Space Complexity: O(V + E) for adjacency list and visited array.
"""

from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node: int) -> int:
            visited[node] = True
            count = 1
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    count += dfs(neighbor)
            return count

        remaining = n
        unreachable_pairs = 0

        for i in range(n):
            if not visited[i]:
                size = dfs(i)
                unreachable_pairs += size * (remaining - size)
                remaining -= size

        return unreachable_pairs
