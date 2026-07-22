"""
Problem: Maximum Width of Binary Tree
LeetCode #: 662
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-width-of-binary-tree/

Approach: Level order traversal (BFS) storing node position index alongside each node. If a parent is at index `i`, its left child is at `2 * i` and right child is at `2 * i + 1`. Width at each level is `last_idx - first_idx + 1`.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for queue storage.
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            _, first_idx = queue[0]
            _, last_idx = queue[-1]
            max_width = max(max_width, last_idx - first_idx + 1)

            for _ in range(level_length):
                node, idx = queue.popleft()
                # Normalize index relative to first_idx to prevent unbounded integer growth
                normalized_idx = idx - first_idx
                if node.left:
                    queue.append((node.left, 2 * normalized_idx))
                if node.right:
                    queue.append((node.right, 2 * normalized_idx + 1))

        return max_width
