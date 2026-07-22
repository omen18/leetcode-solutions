"""
Problem: Longest Path With Different Adjacent Characters
LeetCode #: 2246
Difficulty: Hard
Link: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

Approach: Post-order DFS tree DP.
Build adjacency tree from parent array. For each node, find the top two longest downward paths
from children with characters different from the current node's character.
Update global maximum with 1 + top1 + top2. Return 1 + top1 for recursive call.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import defaultdict
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = defaultdict(list)
        for node, p in enumerate(parent):
            if p != -1:
                children[p].append(node)

        max_path = 0

        def dfs(node: int) -> int:
            nonlocal max_path
            top1, top2 = 0, 0

            for child in children[node]:
                child_len = dfs(child)
                if s[child] != s[node]:
                    if child_len > top1:
                        top2 = top1
                        top1 = child_len
                    elif child_len > top2:
                        top2 = child_len

            max_path = max(max_path, 1 + top1 + top2)
            return 1 + top1

        dfs(0)
        return max_path
