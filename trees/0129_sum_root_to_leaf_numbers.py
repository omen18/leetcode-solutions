"""
Problem: Sum Root to Leaf Numbers
LeetCode #: 0129
Difficulty: Medium
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/

Approach: DFS preorder traversal. Maintain running sum: curr_sum = curr_sum * 10 + val.
At leaf nodes, add the accumulated number to total sum.
Time Complexity: O(N)
Space Complexity: O(H) where H is tree height.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                return curr_sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)

        return dfs(root, 0)
