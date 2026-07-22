"""
Problem: Validate Binary Search Tree
LeetCode #: 98
Difficulty: Medium
Link: https://leetcode.com/problems/validate-binary-search-tree/

Approach: Recursively validate each node's value falls within a valid range (low, high). Left child range becomes (low, node.val) and right child range becomes (node.val, high).
Time Complexity: O(N) where N is the number of nodes in the tree.
Space Complexity: O(N) due to recursion stack in skewed tree case (O(H) where H is height).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))
