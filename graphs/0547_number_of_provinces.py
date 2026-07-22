"""
Problem: Number of Provinces
LeetCode #: 547
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-provinces/

Approach: DFS / Connected Components. Iterate over each city; if not visited, launch DFS
to visit all cities in the same connected component and increment the province count.

Time Complexity: O(N^2) where N is the number of cities.
Space Complexity: O(N) for visited tracking and recursion stack.
"""

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(node: int) -> None:
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1

        return provinces
