"""
Problem: Kth Smallest Element in a BST
LeetCode #: 230
Difficulty: Medium
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Approach: Inorder traversal of a BST visits nodes in strictly ascending sorted order. Using an iterative stack-based inorder traversal, stop and return the node's value when the k-th node is visited.
Time Complexity: O(H + k) where H is tree height.
Space Complexity: O(H) for the explicit stack.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

        return -1
