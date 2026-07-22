"""
Problem: Course Schedule IV
LeetCode #: 1462
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule-iv/

Approach: Transitive Closure via Floyd-Warshall Algorithm.
Maintain a 2D boolean matrix `is_prereq` indicating reachability between course nodes.
Propagate prerequisite relationships across intermediate nodes using Floyd-Warshall.

Time Complexity: O(N^3 + Q) where N is numCourses and Q is number of queries.
Space Complexity: O(N^2) for adjacency matrix.
"""

from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        is_prereq = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            is_prereq[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    is_prereq[i][j] = is_prereq[i][j] or (
                        is_prereq[i][k] and is_prereq[k][j]
                    )

        return [is_prereq[u][v] for u, v in queries]
