"""
Problem: Populating Next Right Pointers in Each Node II
LeetCode #: 0117
Difficulty: Medium
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Approach: Use a dummy node to track the head of the next level linked list.
Traverse the current level using next pointers while constructing the next level's linked list.
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
        curr = root
        while curr:
            dummy = Node(0)
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
        return root
