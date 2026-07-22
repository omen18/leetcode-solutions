"""
Problem: Serialize and Deserialize Binary Tree
LeetCode #: 0297
Difficulty: Hard
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Approach: Preorder DFS string encoding.
Serialize: Recursively visit root, left, right. Represent null nodes as '#'.
Deserialize: Split string by comma into a deque and recursively reconstruct tree preorder.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        vals = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                vals.append('#')
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        nodes = deque(data.split(','))

        def dfs() -> Optional[TreeNode]:
            val = nodes.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
