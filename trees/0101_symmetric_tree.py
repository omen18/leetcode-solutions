"""
Problem: Symmetric Tree
LeetCode #: 101
Difficulty: Easy
Link: https://leetcode.com/problems/symmetric-tree/

Approach: Recursive check comparing left node with opposite right node.
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False
            return check(n1.left, n2.right) and check(n1.right, n2.left)

        return check(root.left, root.right) if root else True


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    print(sol.isSymmetric(root))  # True
