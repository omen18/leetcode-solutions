"""
Problem: Possible Bipartition
LeetCode #: 886
Difficulty: Medium
Link: https://leetcode.com/problems/possible-bipartition/

Approach: Model dislikes as an undirected graph. Determine if the graph can be partitioned into two sets by checking if it is bipartite (2-colorable).
Time Complexity: O(V + E) where V is n and E is dislikes length.
Space Complexity: O(V + E) for adjacency list, color array, and stack.
"""

from typing import List
from collections import defaultdict

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)

        color = [0] * (n + 1)

        def dfs(node: int, c: int) -> bool:
            color[node] = c
            for neighbor in adj[node]:
                if color[neighbor] == c:
                    return False
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
            return True

        for i in range(1, n + 1):
            if color[i] == 0 and not dfs(i, 1):
                return False

        return True
