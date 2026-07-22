"""
Problem: Lowest Common Ancestor of a Binary Tree IV
LeetCode #: 1676
Difficulty: Medium
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

Approach: Recursive post-order DFS. Store target nodes in a set.
If the current node is None or in the target set, return it.
If both left and right subtrees return non-None, the current node is their LCA.
Otherwise, return the non-None child response.
Time Complexity: O(N)
Space Complexity: O(H + M) where H is tree height and M is number of target nodes.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: List['TreeNode']) -> 'TreeNode':
        node_set = set(nodes)

        def dfs(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr or curr in node_set:
                return curr

            left = dfs(curr.left)
            right = dfs(curr.right)

            if left and right:
                return curr
            return left if left else right

        return dfs(root)
