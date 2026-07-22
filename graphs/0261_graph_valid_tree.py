"""
Problem: Graph Valid Tree
LeetCode #: 261
Difficulty: Medium
Link: https://leetcode.com/problems/graph-valid-tree/

Approach: A graph with n nodes is a valid tree if and only if it has exactly n - 1 edges and is fully connected with no cycles. Use Disjoint Set Union (DSU) to check for cycle creation.
Time Complexity: O(N * \alpha(N)) using union-find with path compression and rank.
Space Complexity: O(N) for parent array.
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

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
                return False

        return True
