"""
Problem: Lowest Common Ancestor of a Binary Tree
LeetCode #: 236
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Approach: Bottom-up recursive DFS traversal. Base cases return root if root is None, p, or q. Recursively process left and right subtrees. If both return non-None values, current node is the LCA. Otherwise return whichever subtree returned non-None.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(H) where H is tree height for recursion stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right
