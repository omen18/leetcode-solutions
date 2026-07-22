"""
Problem: Number of Connected Components in an Undirected Graph
LeetCode #: 323
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Approach: Disjoint Set Union (DSU). Start with n components. Decrement component count whenever union succeeds for an edge.
Time Complexity: O(V + E * \alpha(V)) where V is n and E is number of edges.
Space Complexity: O(V) for DSU parent array.
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        components = n

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> bool:
            nonlocal components
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                components -= 1
                return True
            return False

        for u, v in edges:
            union(u, v)

        return components
