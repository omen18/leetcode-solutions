"""
Problem: Smallest String With Swaps
LeetCode #: 1202
Difficulty: Medium
Link: https://leetcode.com/problems/smallest-string-with-swaps/

Approach: Union-Find (Disjoint Set Union). Characters at indices connected directly or indirectly via swap pairs form connected components. For each component, sort the indices and characters independently, then reconstruct the smallest possible string.
Time Complexity: O(N log N + P * alpha(N))
Space Complexity: O(N)
"""

from typing import List
from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s)))

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> None:
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for u, v in pairs:
            union(u, v)

        components = defaultdict(list)
        for i in range(len(s)):
            components[find(i)].append(i)

        res = list(s)
        for indices in components.values():
            chars = sorted(res[i] for i in indices)
            for idx, ch in zip(indices, chars):
                res[idx] = ch

        return "".join(res)
