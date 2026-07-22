"""
Problem: Delete Nodes And Return Forest
LeetCode #: 1110
Difficulty: Medium
Link: https://leetcode.com/problems/delete-nodes-and-return-forest/

Approach: Bottom-up postorder DFS traversal using a hash set for quick lookup of nodes to delete. If a node is deleted, its non-null children become roots of new trees in the forest.
Time Complexity: O(N) where N is number of nodes.
Space Complexity: O(N + D) where D is size of to_delete array.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None

            deleted = node.val in to_delete_set

            if is_root and not deleted:
                forest.append(node)

            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)

            return None if deleted else node

        dfs(root, True)
        return forest
