"""
Problem: Remove Nth Node From End of List
LeetCode #: 19
Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Approach: Use two pointers (fast and slow) with a dummy head. Advance the fast pointer n steps ahead, then advance both pointers together until fast reaches the end. Update slow's next pointer to skip the target node.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
