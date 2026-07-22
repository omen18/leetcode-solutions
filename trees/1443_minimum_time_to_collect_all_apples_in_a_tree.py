"""
Problem: Minimum Time to Collect All Apples in a Tree
LeetCode #: 1443
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

Approach: Construct undirected graph adjacency list from edges. Run DFS starting from node 0 (with parent tracking to prevent cycles). Subtree returns total time taken to traverse children that contain apples. If child subtree time > 0 or child has an apple, add child's sub-time + 2 (for travel to & back) to current total.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for adjacency list and DFS recursion stack.
"""

from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(curr: int, parent: int) -> int:
            total_time = 0

            for neighbor in adj[curr]:
                if neighbor == parent:
                    continue
                child_time = dfs(neighbor, curr)
                if child_time > 0 or hasApple[neighbor]:
                    total_time += child_time + 2

            return total_time

        return dfs(0, -1)
