"""
Problem: Flip Equivalent Binary Trees
LeetCode #: 951
Difficulty: Medium
Link: https://leetcode.com/problems/flip-equivalent-binary-trees/

Approach: Recursive DFS. Two trees are flip equivalent if:
- Both nodes are None (True)
- One node is None or their values differ (False)
- Subtrees are equivalent without flipping OR subtrees are equivalent with flipping.
Time Complexity: O(min(N1, N2)) where N1, N2 are total nodes in root1 and root2.
Space Complexity: O(min(H1, H2)) where H1, H2 are tree heights.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        # Check un-flipped match
        no_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if no_flip:
            return True

        # Check flipped match
        flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return flip
