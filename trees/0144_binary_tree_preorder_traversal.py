"""
Problem: Binary Tree Preorder Traversal
LeetCode #: 144
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

Approach: Iterative preorder traversal with explicit stack.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(sol.preorderTraversal(root))  # [1, 2, 3]
