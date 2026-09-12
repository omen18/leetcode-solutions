"""
Problem: Binary Tree Level Order Traversal II
LeetCode #: 107
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Approach: BFS level order traversal reversed for bottom-up ordering.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.levelOrderBottom(root))  # [[15, 7], [9, 20], [3]]
