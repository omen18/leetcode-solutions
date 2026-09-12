"""
Problem: Binary Tree Postorder Traversal
LeetCode #: 145
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-postorder-traversal/

Approach: Modified preorder (root -> right -> left) then reverse result for postorder.
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(sol.postorderTraversal(root))  # [3, 2, 1]
