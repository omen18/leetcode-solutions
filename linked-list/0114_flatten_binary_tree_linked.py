"""
Problem: Flatten Binary Tree to Linked List
LeetCode #: 114
Difficulty: Medium
Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Approach: Morris-like Traversal / Space-Efficient Pointer Rewiring. For each node, if it has a left child, find the rightmost node of the left subtree and attach the current right subtree to its right. Then move the left subtree to the right.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional

# Definition for a binary tree node.
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
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right
