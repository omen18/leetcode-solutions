"""
Problem: Find Largest Value in Each Tree Row
LeetCode #: 515
Difficulty: Medium
Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Approach: Level order traversal (BFS) using queue. For each level, track the maximum node value encountered and append to final output list.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for BFS queue.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_max = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(int(level_max))

        return result
