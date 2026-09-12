"""
Problem: Recover Binary Search Tree
LeetCode #: 99
Difficulty: Medium
Link: https://leetcode.com/problems/recover-binary-search-tree/

Approach: Inorder traversal finding two swapped nodes violating BST sorted order.
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
            prev = node
            inorder(node.right)

        inorder(root)
        if first and second:
            first.val, second.val = second.val, first.val


if __name__ == "__main__":
    sol = Solution()
    r = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    sol.recoverTree(r)
    print(r.val)  # 3
