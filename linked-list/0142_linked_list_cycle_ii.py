"""
Problem: Linked List Cycle II
LeetCode #: 142
Difficulty: Medium
Link: https://leetcode.com/problems/linked-list-cycle-ii/

Approach: Use Floyd's Tortoise and Hare algorithm. If slow and fast pointers meet, a cycle exists. Reset a pointer to the head of the list and advance both head and slow pointers one step at a time; their meeting node is the cycle start.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Step 1: Determine if a cycle exists using fast and slow pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        # Step 2: Find the entry point of the cycle
        entry = head
        while entry != slow:
            entry = entry.next
            slow = slow.next

        return entry
