"""
Problem: Detonate the Maximum Bombs
LeetCode #: 2101
Difficulty: Medium
Link: https://leetcode.com/problems/detonate-the-maximum-bombs/

Approach: Directed Graph Construction + BFS.
1. Connect directed edge i -> j if bomb i's blast radius covers bomb j: (x1 - x2)^2 + (y1 - y2)^2 <= r1^2.
2. Run BFS starting from each bomb i to find the total size of its detonation chain reaction.
3. Return the maximum chain length discovered.

Time Complexity: O(N^3) where N is the number of bombs (N <= 100).
Space Complexity: O(N^2) for storing graph edges and visited sets.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def maximumDetonations(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1**2:
                    adj[i].append(j)

        def bfs(start: int) -> int:
            queue = deque([start])
            visited = {start}
            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)

        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, bfs(i))

        return max_bombs
