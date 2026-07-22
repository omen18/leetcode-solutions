"""
Problem: Add Two Numbers II
LeetCode #: 445
Difficulty: Medium
Link: https://leetcode.com/problems/add-two-numbers-ii/

Approach: Push node values from both linked lists onto two separate stacks to process digits in reverse order without modifying the original input lists. Pop values from the stacks, calculate digit sums and carries, and prepend new nodes to construct the result list.
Time Complexity: O(N + M) where N and M are the lengths of the input lists.
Space Complexity: O(N + M) for the stacks.
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
        stack1, stack2 = [], []

        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next

        head = None
        carry = 0

        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            new_node = ListNode(total % 10)
            new_node.next = head
            head = new_node

        return head
