"""
Problem: Number of Operations to Make Network Connected
LeetCode #: 1319
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/

Approach: A network of n computers requires at least n - 1 cables to be fully connected. If total connections < n - 1, return -1. Otherwise, count connected components C using DSU; result is C - 1.
Time Complexity: O(V + E * \alpha(V)) where V is n and E is connections length.
Space Complexity: O(V) for DSU parent structure.
"""

from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))
        components = n

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> None:
            nonlocal components
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                components -= 1

        for u, v in connections:
            union(u, v)

        return components - 1
