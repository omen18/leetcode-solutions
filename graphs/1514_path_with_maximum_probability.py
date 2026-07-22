"""
Problem: Path with Maximum Probability
LeetCode #: 1514
Difficulty: Medium
Link: https://leetcode.com/problems/path-with-maximum-probability/

Approach: Modified Dijkstra's Algorithm using a Max-Heap. Maintain maximum probability path to each node. Pop node with highest probability and update neighbor probabilities.
Time Complexity: O(E log V)
Space Complexity: O(V + E)
"""

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        heap = [(-1.0, start_node)]

        while heap:
            curr_prob, u = heapq.heappop(heap)
            curr_prob = -curr_prob

            if u == end_node:
                return curr_prob

            if curr_prob < max_prob[u]:
                continue

            for v, prob in adj[u]:
                next_prob = curr_prob * prob
                if next_prob > max_prob[v]:
                    max_prob[v] = next_prob
                    heapq.heappush(heap, (-next_prob, v))

        return 0.0
