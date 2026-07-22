"""
Problem: Shortest Path Visiting All Nodes
LeetCode #: 847
Difficulty: Hard
Link: https://leetcode.com/problems/shortest-path-visiting-all-nodes/

Approach: Bitmask BFS.
Encode the set of visited nodes in a bitmask. The state is represented as `(curr_node, visited_bitmask)`.
Start BFS simultaneously from all nodes (multisource BFS with distance 0).
The search terminates as soon as any state achieves mask `(1 << N) - 1`.

Time Complexity: O(N * 2^N) where N is number of nodes (N <= 12).
Space Complexity: O(N * 2^N) for storing visited states.
"""

from collections import deque
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        target_mask = (1 << n) - 1
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}

        while queue:
            node, mask, dist = queue.popleft()

            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if next_mask == target_mask:
                    return dist + 1

                if (neighbor, next_mask) not in visited:
                    visited.add((neighbor, next_mask))
                    queue.append((neighbor, next_mask, dist + 1))

        return 0
