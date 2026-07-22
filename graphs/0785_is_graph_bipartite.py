"""
Problem: Is Graph Bipartite?
LeetCode #: 785
Difficulty: Medium
Link: https://leetcode.com/problems/is-graph-bipartite/

Approach: Try 2-coloring the graph using BFS or DFS. Color unvisited components starting with color 1. If an adjacent vertex has the same color, graph is not bipartite.
Time Complexity: O(V + E) where V is graph length and E total edges.
Space Complexity: O(V) for color array and traversal queue/stack.
"""

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n  # 0: uncolored, 1: red, -1: blue

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
            return True

        for i in range(n):
            if color[i] == 0 and not dfs(i, 1):
                return False

        return True
