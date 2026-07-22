"""
Problem: All Nodes Distance K in Binary Tree
LeetCode #: 863
Difficulty: Medium
Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Approach: First, traverse the tree with DFS to map each node to its parent pointer, creating an undirected graph graph. Then perform BFS starting from target node up to distance K, keeping track of visited nodes.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N) for parent mapping and BFS queue.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}

        def mark_parents(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if not node:
                return
            parents[node] = parent
            mark_parents(node.left, node)
            mark_parents(node.right, node)

        mark_parents(root, None)

        queue = deque([(target, 0)])
        visited = {target}
        result = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                result.append(node.val)
            elif dist < k:
                neighbors = [node.left, node.right, parents[node]]
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return result
