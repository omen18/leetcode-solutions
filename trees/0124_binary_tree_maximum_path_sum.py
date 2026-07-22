"""
Problem: Binary Tree Maximum Path Sum
LeetCode #: 0124
Difficulty: Hard
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Approach: DFS post-order traversal. Compute the maximum non-negative contribution from left
and right subtrees. Update global maximum path sum with left + right + node.val.
Return node.val + max(left, right) for recursive caller.
Time Complexity: O(N)
Space Complexity: O(H)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node:
                return 0

            # Max contribution from left and right children (ignore negative paths)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Max path sum passing through current node
            current_max = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_max)

            # Max gain current node can contribute to its parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum
