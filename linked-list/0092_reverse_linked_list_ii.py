"""
Problem: Reverse Linked List II
LeetCode #: 92
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-linked-list-ii/

Approach: Use a dummy head to handle edge cases where left=1. Traverse to the node immediately preceding the left position. Perform head-insertion in-place for each node in the sublist from left to right.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next
