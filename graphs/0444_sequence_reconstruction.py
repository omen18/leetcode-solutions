"""
Problem: Sequence Reconstruction
LeetCode #: 444
Difficulty: Medium
Link: https://leetcode.com/problems/sequence-reconstruction/

Approach: Topological Sort with BFS. Build a directed graph from adjacent elements in the given sequences. Verify that at each step of topological sorting, there is exactly one node with indegree 0, ensuring the sequence reconstructs `nums` uniquely.
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        adj = defaultdict(set)
        indegree = {i: 0 for i in range(1, n + 1)}
        nodes_present = set()

        for seq in sequences:
            for num in seq:
                if num not in indegree:
                    return False
                nodes_present.add(num)
            for i in range(len(seq) - 1):
                u, v = seq[i], seq[i + 1]
                if v not in adj[u]:
                    adj[u].add(v)
                    indegree[v] += 1

        if len(nodes_present) != n:
            return False

        queue = deque([node for node in indegree if indegree[node] == 0])
        res = []

        while queue:
            if len(queue) > 1:
                return False
            curr = queue.popleft()
            res.append(curr)

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res == nums
