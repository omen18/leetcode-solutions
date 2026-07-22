"""
Problem: Time Needed to Inform All Employees
LeetCode #: 1376
Difficulty: Medium
Link: https://leetcode.com/problems/time-needed-to-inform-all-employees/

Approach: Build adjacency tree of manager -> subordinates. Use Depth-First Search (DFS) from headID to find maximum total informTime along any path to a leaf node.
Time Complexity: O(N) where N is number of employees.
Space Complexity: O(N) for adjacency list and recursion stack.
"""

from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for emp in range(n):
            if manager[emp] != -1:
                adj[manager[emp]].append(emp)

        def dfs(curr: int) -> int:
            max_time = 0
            for sub in adj[curr]:
                max_time = max(max_time, dfs(sub))
            return informTime[curr] + max_time

        return dfs(headID)
