"""
Problem: Course Schedule II
LeetCode #: 210
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule-ii/

Approach: Kahn's Algorithm for Topological Sorting using BFS and in-degrees. Appends nodes with 0 in-degree to ordering array. If output length matches numCourses, return ordering, else empty array.
Time Complexity: O(V + E) where V is numCourses and E is prerequisites.
Space Complexity: O(V + E) for storing adjacency list, in-degrees, and result queue.
"""

from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []
