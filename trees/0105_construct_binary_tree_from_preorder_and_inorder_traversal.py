"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
LeetCode #: 105
Difficulty: Medium
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Approach: The first element in preorder traversal is always the root. Find this root's index in the inorder array using a hash map to divide inorder elements into left and right subtrees. Recursively build subtrees.
Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(N) for hash map and recursion stack.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None

            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            index = inorder_idx_map[root_val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)
