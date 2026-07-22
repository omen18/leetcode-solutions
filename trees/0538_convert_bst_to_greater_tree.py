"""
Problem: Convert BST to Greater Tree
LeetCode #: 538
Difficulty: Medium
Link: https://leetcode.com/problems/convert-bst-to-greater-tree/

Approach: Perform a reverse inorder traversal (Right -> Node -> Left). Maintain a running sum of node values visited so far and update each node's value with this running sum.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(H) where H is height of the tree for recursion stack.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def reverse_inorder(node: Optional[TreeNode]):
            if not node:
                return
            reverse_inorder(node.right)
            self.total += node.val
            node.val = self.total
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
