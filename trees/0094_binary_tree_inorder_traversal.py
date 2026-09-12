"""
Problem: Binary Tree Inorder Traversal
LeetCode #: 94
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Approach: Iterative stack traversal (left, root, right).
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(sol.inorderTraversal(root))  # [1, 3, 2]
