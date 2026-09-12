"""
Problem: Path Sum
LeetCode #: 112
Difficulty: Easy
Link: https://leetcode.com/problems/path-sum/

Approach: DFS preorder: subtract current node value from targetSum until reaching a leaf.
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
    print(sol.hasPathSum(root, 22))  # True
