"""
Problem: Check Completeness of a Binary Tree
LeetCode #: 958
Difficulty: Medium
Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/

Approach: Perform level order traversal (BFS) pushing all nodes (including None) into queue. Once a None node is popped, all subsequent nodes in the queue must also be None for the tree to be complete.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for BFS queue.
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        encountered_none = False

        while queue:
            node = queue.popleft()

            if not node:
                encountered_none = True
            else:
                if encountered_none:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True
