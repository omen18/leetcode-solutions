"""
Problem: Reorder List
LeetCode #: 143
Difficulty: Medium
Link: https://leetcode.com/problems/reorder-list/

Approach: 
1. Find the middle of the linked list using fast and slow pointers.
2. Reverse the second half of the linked list.
3. Interleave the first half and the reversed second half in-place.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find middle of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # break the link between first and second halves

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 3. Interleave two halves: head (first half) and prev (reversed second half)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
