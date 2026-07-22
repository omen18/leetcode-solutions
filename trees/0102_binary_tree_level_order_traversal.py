"""
Problem: Binary Tree Level Order Traversal
LeetCode #: 102
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Approach: Breadth-First Search (BFS) using a queue to traverse the binary tree level by level. For each level, process all current nodes, collect their values, and enqueue their children.
Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(N) to store nodes in queue and output.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result
