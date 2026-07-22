"""
Problem: Minimum Number of Vertices to Reach All Nodes
LeetCode #: 1557
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

Approach: In a Directed Acyclic Graph (DAG), any node with an in-degree of 0 cannot be reached from any other node and MUST be included. All other nodes with in-degree > 0 can be reached from in-degree 0 nodes.
Time Complexity: O(V + E) where V is n and E is edges length.
Space Complexity: O(V) for tracking in-degrees.
"""

from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_incoming = [False] * n
        for u, v in edges:
            has_incoming[v] = True

        return [i for i in range(n) if not has_incoming[i]]
