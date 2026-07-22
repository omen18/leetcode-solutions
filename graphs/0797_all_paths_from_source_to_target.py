"""
Problem: All Paths From Source to Target
LeetCode #: 797
Difficulty: Medium
Link: https://leetcode.com/problems/all-paths-from-source-to-target/

Approach: Depth-First Search with backtracking to explore all possible paths from source node 0 to target node n-1 in a Directed Acyclic Graph (DAG).
Time Complexity: O(2^V * V) since there could be 2^(V-1) paths of maximum length V.
Space Complexity: O(V) for recursion stack.
"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []

        def dfs(node: int, path: List[int]) -> None:
            if node == target:
                res.append(list(path))
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])
        return res
