"""
Problem: Redundant Connection II
LeetCode #: 685
Difficulty: Hard
Link: https://leetcode.com/problems/redundant-connection-ii/

Approach: Case Analysis with Union-Find (DSU).
A valid directed tree structure can be violated in two ways when an extra edge is added:
1. A node gains 2 parents (in-degree = 2).
2. A directed cycle is introduced.

We identify two-parent candidates `cand1` and `cand2`. Then we execute DSU ignoring `cand2`:
- If a cycle occurs and dual parents exist, return `cand1`.
- If a cycle occurs and no dual parents exist, return the cycle-closing edge.
- If no cycle occurs, return `cand2`.

Time Complexity: O(N * α(N)) where N is number of nodes/edges.
Space Complexity: O(N) for DSU and parent array tracking.
"""

from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        cand1 = None
        cand2 = None

        # Check for node with 2 parents
        for u, v in edges:
            if parent[v] != v:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break
            parent[v] = u

        # Run Union-Find skipping cand2
        dsu_parent = list(range(n + 1))

        def find(i: int) -> int:
            if dsu_parent[i] != i:
                dsu_parent[i] = find(dsu_parent[i])
            return dsu_parent[i]

        def union(i: int, j: int) -> bool:
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False
            dsu_parent[root_i] = root_j
            return True

        for u, v in edges:
            if [u, v] == cand2:
                continue
            if not union(u, v):
                if cand1:
                    return cand1
                return [u, v]

        return cand2
