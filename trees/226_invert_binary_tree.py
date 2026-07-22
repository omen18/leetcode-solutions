"""
Problem: Invert Binary Tree
LeetCode #: 226
Difficulty: Easy
Link: https://leetcode.com/problems/invert-binary-tree/

Approach: Recursive DFS — swap left and right children at every node.
Time Complexity: O(n)
Space Complexity: O(h) where h = height of tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
