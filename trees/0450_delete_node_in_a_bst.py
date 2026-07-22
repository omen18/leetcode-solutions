"""
Problem: Delete Node in a BST
LeetCode #: 450
Difficulty: Medium
Link: https://leetcode.com/problems/delete-node-in-a-bst/

Approach: Recursive search for key in BST. When node to delete is found:
- If it has no left child, return right child.
- If it has no right child, return left child.
- If both children exist, find the inorder successor (min node in right subtree), swap node's val with successor's val, and recursively delete successor from right subtree.
Time Complexity: O(H) where H is tree height.
Space Complexity: O(H) for recursion stack.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node with two children: find min in right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, curr.val)

        return root
