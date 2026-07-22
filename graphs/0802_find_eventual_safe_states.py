"""
Problem: Find Eventual Safe States
LeetCode #: 802
Difficulty: Medium
Link: https://leetcode.com/problems/find-eventual-safe-states/

Approach: Detect cycles using 3-color DFS. A node is safe if all outgoing paths lead to terminal nodes (no cycle reachable). Mark nodes: 0 = unvisited, 1 = visiting, 2 = safe.
Time Complexity: O(V + E) where V is number of nodes and E is total edges.
Space Complexity: O(V) for color array and recursion stack.
"""

from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n  # 0: unvisited, 1: visiting, 2: safe

        def dfs(node: int) -> bool:
            if color[node] > 0:
                return color[node] == 2
            
            color[node] = 1  # mark visiting
            for neighbor in graph[node]:
                if color[neighbor] == 1 or not dfs(neighbor):
                    return False
            
            color[node] = 2  # mark safe
            return True

        return [i for i in range(n) if dfs(i)]
