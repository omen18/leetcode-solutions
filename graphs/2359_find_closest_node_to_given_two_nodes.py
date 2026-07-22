"""
Problem: Find Closest Node to Given Two Nodes
LeetCode #: 2359
Difficulty: Medium
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

Approach: Compute shortest distances from node1 and node2 to all reachable nodes using BFS/graph traversal. Iterate through all nodes to find the node index that minimizes max(dist1[i], dist2[i]).
Time Complexity: O(N) where N is total number of nodes.
Space Complexity: O(N) for distance tracking arrays.
"""

from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def get_distances(start: int) -> List[int]:
            dist = [-1] * n
            d = 0
            curr = start
            while curr != -1 and dist[curr] == -1:
                dist[curr] = d
                d += 1
                curr = edges[curr]
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_max_dist = float('inf')
        ans = -1

        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                max_d = max(dist1[i], dist2[i])
                if max_d < min_max_dist:
                    min_max_dist = max_d
                    ans = i

        return ans
