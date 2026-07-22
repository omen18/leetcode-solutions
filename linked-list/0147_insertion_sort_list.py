"""
Problem: Insertion Sort List
LeetCode #: 147
Difficulty: Medium
Link: https://leetcode.com/problems/insertion-sort-list/

Approach: Dummy Head Pointer Rewiring. Maintain a sorted portion with a dummy head. For each node in the unsorted list, find its correct insertion position in the sorted chain and update the links.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head

        while curr:
            nxt = curr.next
            
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return dummy.next
