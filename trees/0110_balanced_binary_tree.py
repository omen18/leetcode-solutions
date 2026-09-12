"""
Problem: Balanced Binary Tree
LeetCode #: 110
Difficulty: Easy
Link: https://leetcode.com/problems/balanced-binary-tree/

Approach: Bottom-up DFS calculating height; return -1 early if unbalanced.
Time Complexity: O(n)
Space Complexity: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.isBalanced(root))  # True
