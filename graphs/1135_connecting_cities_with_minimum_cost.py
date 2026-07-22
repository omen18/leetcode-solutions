"""
Problem: Connecting Cities With Minimum Cost
LeetCode #: 1135
Difficulty: Medium
Link: https://leetcode.com/problems/connecting-cities-with-minimum-cost/

Approach: Kruskal's Algorithm (Minimum Spanning Tree with Union-Find).
Sort connections by cost. Iterate through edges, uniting components with DSU.
If we use n - 1 edges, return total cost; otherwise, return -1 if graph is disconnected.

Time Complexity: O(E log E + E * α(N)) where E is number of connections and N is number of cities.
Space Complexity: O(N) for Union-Find structure.
"""

from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        total_cost = 0
        edges_used = 0

        for u, v, cost in connections:
            if uf.union(u, v):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    return total_cost

        return total_cost if n == 1 else -1
