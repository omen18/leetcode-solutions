"""
Problem: Convert Sorted List to Binary Search Tree
LeetCode #: 109
Difficulty: Medium
Link: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Approach: Convert the linked list into an array for O(1) random access, then recursively build the height-balanced BST by selecting the middle element as the root of each subtree.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        def build_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(vals[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node

        return build_tree(0, len(vals) - 1)
