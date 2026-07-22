"""
Problem: Flatten a Multilevel Doubly Linked List
LeetCode #: 430
Difficulty: Medium
Link: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Approach: Iterate through the doubly linked list. Whenever a node with a child is encountered, find the tail of the child list, splice the child list between current node and current.next, and set child pointer to None.
Time Complexity: O(N) where N is the total number of nodes in the multilevel list.
Space Complexity: O(1) extra space.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        while curr:
            if curr.child:
                nxt = curr.next

                # Find tail of child list
                child_tail = curr.child
                while child_tail.next:
                    child_tail = child_tail.next

                # Splice child list between curr and nxt
                child_tail.next = nxt
                if nxt:
                    nxt.prev = child_tail

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            curr = curr.next

        return head
