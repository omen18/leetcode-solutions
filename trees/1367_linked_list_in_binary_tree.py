"""
Problem: Linked List in Binary Tree
LeetCode #: 1367
Difficulty: Medium
Link: https://leetcode.com/problems/linked-list-in-binary-tree/

Approach: Double DFS traversal. For each tree node in main DFS (`isSubPath`), attempt matching the linked list path starting at that node via secondary DFS (`check_path`).
Time Complexity: O(N * min(H, L)) where N is number of tree nodes, H is height, L is linked list length.
Space Complexity: O(H) for recursion stack.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def check_path(head_node: Optional[ListNode], tree_node: Optional[TreeNode]) -> bool:
            if not head_node:
                return True
            if not tree_node:
                return False
            if head_node.val != tree_node.val:
                return False
            return (check_path(head_node.next, tree_node.left) or
                    check_path(head_node.next, tree_node.right))

        if not root:
            return False

        return (check_path(head, root) or
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right))
