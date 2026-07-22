"""
Problem: Pacific Atlantic Water Flow
LeetCode #: 417
Difficulty: Medium
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Approach: Reverse the flow problem by running DFS/BFS from ocean borders inwards (uphill: neighbor height >= current height). Find intersection of cells reachable by both oceans.
Time Complexity: O(M * N) where M and N are grid dimensions.
Space Complexity: O(M * N) for visited sets and recursion stack.
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r: int, c: int, reachable: set) -> None:
            reachable.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in reachable and
                        heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols - 1, atlantic_reachable)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows - 1, c, atlantic_reachable)

        return list(pacific_reachable & atlantic_reachable)
