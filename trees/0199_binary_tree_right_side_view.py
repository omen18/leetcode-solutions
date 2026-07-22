"""
Problem: Binary Tree Right Side View
LeetCode #: 199
Difficulty: Medium
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Approach: Perform level order traversal (BFS). The last element encountered at each level represents the node visible from the right side.
Time Complexity: O(N) where N is the number of nodes in the tree.
Space Complexity: O(N) for storing queue nodes and level results.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if i == level_length - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
