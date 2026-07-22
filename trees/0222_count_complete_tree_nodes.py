"""
Problem: Count Complete Tree Nodes
LeetCode #: 0222
Difficulty: Easy
Link: https://leetcode.com/problems/count-complete-tree-nodes/

Approach: Compare left-most and right-most height. If equal, node count is 2^h - 1.
Otherwise, recursively count left and right subtrees.
Time Complexity: O((log N)^2)
Space Complexity: O(log N)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_left_height(node: Optional[TreeNode]) -> int:
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def get_right_height(node: Optional[TreeNode]) -> int:
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        left_h = get_left_height(root)
        right_h = get_right_height(root)

        if left_h == right_h:
            return (1 << left_h) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
