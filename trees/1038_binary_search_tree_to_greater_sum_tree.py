"""
Problem: Binary Search Tree to Greater Sum Tree
LeetCode #: 1038
Difficulty: Medium
Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Approach: Reverse Inorder Traversal (Right -> Node -> Left). Maintain a running accumulated sum of all visited nodes and update node values in place.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(H) where H is tree height for recursion stack.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.running_sum = 0

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.right)
            self.running_sum += node.val
            node.val = self.running_sum
            traverse(node.left)

        traverse(root)
        return root
