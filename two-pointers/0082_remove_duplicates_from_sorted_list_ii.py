"""
Problem: Remove Duplicates from Sorted List II
LeetCode #: 82
Difficulty: Medium
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Approach: Use a dummy node preceding head. Traverse list with a pointer `prev`. If node values equal next node values, skip all nodes with that value.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return dummy.next
