"""
Problem: Redundant Connection
LeetCode #: 684
Difficulty: Medium
Link: https://leetcode.com/problems/redundant-connection/

Approach: Disjoint Set Union (DSU). Process edges sequentially. The first edge connecting two vertices that are already in the same connected component forms a cycle and is redundant.
Time Complexity: O(N * \alpha(N)) where N is the number of edges.
Space Complexity: O(N) for DSU structures.
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False
            parent[root_i] = root_j
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
