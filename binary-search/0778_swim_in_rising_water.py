"""
Problem: Swim in Rising Water
LeetCode #: 778
Difficulty: Hard
Link: https://leetcode.com/problems/swim-in-rising-water/

Approach: Binary search on water level `t` in range [grid[0][0], n^2 - 1]. For a candidate `t`, check connectivity from (0,0) to (n-1, n-1) using BFS/DFS considering only cells with height <= t.
Time Complexity: O(n^2 * log(n^2))
Space Complexity: O(n^2) for BFS queue and visited set
"""

from collections import deque
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def can_reach(t: int) -> bool:
            if grid[0][0] > t:
                return False
            visited = {(0, 0)}
            queue = deque([(0, 0)])

            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and grid[nr][nc] <= t
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        left, right = grid[0][0], n * n - 1
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
