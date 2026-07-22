"""
Problem: Vertical Order Traversal of a Binary Tree
LeetCode #: 0987
Difficulty: Hard
Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Approach: Track coordinates (col, row) for each node via DFS/BFS.
Collect tuples of (col, row, val), sort them by column, then row, then value.
Group values by column to produce vertical order output.
Time Complexity: O(N log N)
Space Complexity: O(N)
"""

from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []

        def dfs(node: Optional[TreeNode], col: int, row: int) -> None:
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)
        nodes.sort(key=lambda x: (x[0], x[1], x[2]))

        res = defaultdict(list)
        for col, row, val in nodes:
            res[col].append(val)

        return [res[col] for col in sorted(res.keys())]
