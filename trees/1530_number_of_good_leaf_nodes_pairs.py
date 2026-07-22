"""
Problem: Number of Good Leaf Nodes Pairs
LeetCode #: 1530
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

Approach: Postorder DFS returning a list of distances of leaf nodes to current node. For each internal node, count pairs (d1, d2) from left and right subtree leaves such that d1 + d2 <= distance. Increment leaf distances by 1 before returning to parent.
Time Complexity: O(N * distance^2) where N is number of nodes.
Space Complexity: O(H * distance) for recursion stack and leaf distance lists.
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.pairs_count = 0

        def dfs(node: TreeNode) -> List[int]:
            if not node:
                return []
            if not node.left and not node.right:
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            for d1 in left_distances:
                for d2 in right_distances:
                    if d1 + d2 <= distance:
                        self.pairs_count += 1

            return [d + 1 for d in left_distances + right_distances if d + 1 < distance]

        dfs(root)
        return self.pairs_count
