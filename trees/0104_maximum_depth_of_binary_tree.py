"""
Problem: Maximum Depth of Binary Tree
LeetCode #: 104
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Approach: DFS postorder traversal: depth = 1 + max(left_depth, right_depth).
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.maxDepth(root))  # 3
