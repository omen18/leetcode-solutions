"""
Problem: Binary Tree Zigzag Level Order Traversal
LeetCode #: 103
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Approach: BFS level order traversal with alternating direction reversal per level.
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        left_to_right = True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right
        return res


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(sol.zigzagLevelOrder(root))  # [[3], [20, 9], [15, 7]]
