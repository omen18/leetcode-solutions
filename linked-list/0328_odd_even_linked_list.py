"""
Problem: Odd Even Linked List
LeetCode #: 328
Difficulty: Medium
Link: https://leetcode.com/problems/odd-even-linked-list/

Approach: Maintain pointers for odd and even nodes. Link odd nodes together and even nodes together in a single pass, then attach the head of the even nodes to the end of the odd list.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head
