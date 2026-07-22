"""
Problem: House Robber III
LeetCode #: 337
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber-iii/

Approach: Dynamic Programming on Trees (Tree DFS). Return a pair (rob_node, skip_node) for each subtree.
- rob_node = root.val + left[1] + right[1] (if we rob root, we cannot rob children)
- skip_node = max(left) + max(right) (if we skip root, we can rob or skip children)
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(H) recursion depth where H is tree height.
"""

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            rob_node = node.val + left[1] + right[1]
            skip_node = max(left) + max(right)

            return (rob_node, skip_node)

        return max(dfs(root))
