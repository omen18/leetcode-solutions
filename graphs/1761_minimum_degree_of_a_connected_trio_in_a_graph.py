"""
Problem: Minimum Degree of a Connected Trio in a Graph
LeetCode #: 1761
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

Approach: Adjacency Matrix + Brute Force Trio Search. Precalculate node degrees and build an adjacency matrix. Iterate over all triplets (u, v, w) with u < v < w. If they form a clique (trio), compute degree as deg[u] + deg[v] + deg[w] - 6.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

from typing import List

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        degrees = [0] * (n + 1)

        for u, v in edges:
            adj[u][v] = True
            adj[v][u] = True
            degrees[u] += 1
            degrees[v] += 1

        min_degree = float('inf')

        for u in range(1, n + 1):
            for v in range(u + 1, n + 1):
                if not adj[u][v]:
                    continue
                for w in range(v + 1, n + 1):
                    if adj[u][w] and adj[v][w]:
                        trio_degree = degrees[u] + degrees[v] + degrees[w] - 6
                        min_degree = min(min_degree, trio_degree)

        return min_degree if min_degree != float('inf') else -1
