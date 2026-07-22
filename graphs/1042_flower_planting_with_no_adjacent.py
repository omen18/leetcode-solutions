"""
Problem: Flower Planting With No Adjacent
LeetCode #: 1042
Difficulty: Medium
Link: https://leetcode.com/problems/flower-planting-with-no-adjacent/

Approach: Greedy Graph Coloring. Since each garden has at most 3 paths (degree <= 3) and there are 4 types of flowers, a valid 4-coloring always exists. For each garden from 1 to n, pick the smallest flower type not used by its adjacent neighbors.
Time Complexity: O(N + E)
Space Complexity: O(N + E)
"""

from typing import List
from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in paths:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)

        result = [0] * n
        for garden in range(n):
            used_colors = {result[neighbor] for neighbor in adj[garden] if result[neighbor] != 0}
            for color in range(1, 5):
                if color not in used_colors:
                    result[garden] = color
                    break

        return result
