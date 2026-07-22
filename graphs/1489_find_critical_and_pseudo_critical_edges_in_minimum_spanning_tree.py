"""
Problem: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
LeetCode #: 1489
Difficulty: Hard
Link: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

Approach: Kruskal's MST Edge Classification.
1. Tag each edge with its original index and sort by weight.
2. Compute standard MST weight `std_weight` via Kruskal's.
3. For each edge i:
   - Exclude edge i: If MST weight increases or graph becomes disconnected, edge i is Critical.
   - Force-include edge i: If MST weight equals `std_weight` (and edge i wasn't Critical), edge i is Pseudo-Critical.

Time Complexity: O(E^2 * α(N)) where E is number of edges and N is number of nodes.
Space Complexity: O(N + E) for DSU structures and augmented edge list.
"""

from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.components = size

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        m = len(edges)
        indexed_edges = [[u, v, w, i] for i, (u, v, w) in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[2])

        def get_mst_weight(skip_edge: int = -1, force_edge: int = -1) -> float:
            uf = UnionFind(n)
            weight = 0

            if force_edge != -1:
                u, v, w = edges[force_edge]
                uf.union(u, v)
                weight += w

            for u, v, w, idx in indexed_edges:
                if idx == skip_edge:
                    continue
                if uf.union(u, v):
                    weight += w

            return weight if uf.components == 1 else float("inf")

        std_weight = get_mst_weight()

        critical = []
        pseudo_critical = []

        for i in range(m):
            if get_mst_weight(skip_edge=i) > std_weight:
                critical.append(i)
            elif get_mst_weight(force_edge=i) == std_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
