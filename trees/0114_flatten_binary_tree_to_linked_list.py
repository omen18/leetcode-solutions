"""
Problem: Flatten Binary Tree to Linked List
LeetCode #: 0114
Difficulty: Medium
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Approach: Morris-style traversal. For each node with a left child, find the rightmost node
in its left subtree, attach the node's right child there, then move the left child to right.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                # Find rightmost node of left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right

                # Re-assign pointers
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right
