"""
Problem: Rotate List
LeetCode #: 61
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-list/

Approach: First, compute the length of the list and connect the tail to the head to form a ring. Then compute the effective rotation count k % length. Move to the new tail (length - k - 1 steps from head), set the new head, and break the ring.
Time Complexity: O(N) where N is the number of nodes in the list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Determine the length of the list and get pointer to the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Connect tail to head to form a cycle
        tail.next = head

        # Find the node just before the new head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
