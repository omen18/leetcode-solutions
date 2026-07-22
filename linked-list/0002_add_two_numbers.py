"""
Problem: Add Two Numbers
LeetCode #: 2
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers/

Approach: Traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous addition. Maintain a dummy head node to simplify list construction.
Time Complexity: O(max(N, M)) where N and M are the lengths of the two linked lists.
Space Complexity: O(max(N, M)) for the returned linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
