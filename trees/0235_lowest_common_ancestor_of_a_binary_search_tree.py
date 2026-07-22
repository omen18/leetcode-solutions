"""
Problem: Lowest Common Ancestor of a Binary Search Tree
LeetCode #: 235
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Approach: Leverage the BST property. Starting at the root, if both p and q have values less than root, LCA is in the left subtree. If both have values greater than root, LCA is in the right subtree. Otherwise, root is the split point and thus the LCA.
Time Complexity: O(H) where H is tree height.
Space Complexity: O(1) iterative approach.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
        return root
