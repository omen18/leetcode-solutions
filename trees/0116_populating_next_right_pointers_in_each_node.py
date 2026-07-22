"""
Problem: Populating Next Right Pointers in Each Node
LeetCode #: 0116
Difficulty: Medium
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

Approach: Level-order traversal utilizing already connected next pointers from previous level.
For a perfect binary tree, connect left child to right child, and right child to next node's left child.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # Connection 1: children of same parent
                head.left.next = head.right
                # Connection 2: children of different parents
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root
