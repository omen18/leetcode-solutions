"""
Problem: Merge In Between Linked Lists
LeetCode #: 1669
Difficulty: Medium
Link: https://leetcode.com/problems/merge-in-between-linked-lists/

Approach: Locate the (a-1)-th node and the (b+1)-th node of list1. Traverse list2 to find its tail node. Connect (a-1)-th node to list2's head, and list2's tail to (b+1)-th node.
Time Complexity: O(N + M) where N is list1 length and M is list2 length.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        node_a = None
        node_b = None

        curr = list1
        for i in range(b + 1):
            if i == a - 1:
                node_a = curr
            curr = curr.next
        node_b = curr

        # Find tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # Splice list2 in between
        node_a.next = list2
        tail2.next = node_b

        return list1
