"""
Problem: Shortest Path with Alternating Colors
LeetCode #: 1129
Difficulty: Medium
Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/

Approach: Breadth-First Search (BFS) using state tuple (node, last_edge_color). Track distances and visited states separately for red (0) and blue (1) incoming edges.
Time Complexity: O(V + E) where V is n and E is total edges.
Space Complexity: O(V + E) for graphs, visited state set, and queue.
"""

from typing import List
from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)

        ans = [-1] * n
        queue = deque([(0, 0, -1)])  # (node, distance, last_color: -1 init, 0 red, 1 blue)
        visited = set([(0, -1)])

        while queue:
            node, dist, last_color = queue.popleft()

            if ans[node] == -1:
                ans[node] = dist

            if last_color != 0:  # next can be red edge
                for neighbor in red_graph[node]:
                    if (neighbor, 0) not in visited:
                        visited.add((neighbor, 0))
                        queue.append((neighbor, dist + 1, 0))

            if last_color != 1:  # next can be blue edge
                for neighbor in blue_graph[node]:
                    if (neighbor, 1) not in visited:
                        visited.add((neighbor, 1))
                        queue.append((neighbor, dist + 1, 1))

        return ans
