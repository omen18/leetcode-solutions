"""
Problem: Evaluate Division
LeetCode #: 399
Difficulty: Medium
Link: https://leetcode.com/problems/evaluate-division/

Approach: Graph BFS. Build a weighted directed graph where an equation A / B = val
corresponds to directed edges A -> B with weight val and B -> A with weight 1.0 / val.
For each query (C, D), search for a path from C to D using BFS while tracking cumulative products.

Time Complexity: O(Q * (V + E)) where Q is the number of queries, V is the number of unique variables, and E is the number of equations.
Space Complexity: O(V + E) for storing the graph adjacency list.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val

        def bfs(src: str, target: str) -> float:
            if src not in graph or target not in graph:
                return -1.0
            if src == target:
                return 1.0

            queue = deque([(src, 1.0)])
            visited = {src}

            while queue:
                curr, curr_product = queue.popleft()
                if curr == target:
                    return curr_product

                for neighbor, weight in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, curr_product * weight))

            return -1.0

        return [bfs(q[0], q[1]) for q in queries]
