"""
Problem: Remove Duplicates From an Unsorted Linked List
LeetCode #: 1836
Difficulty: Medium
Link: https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

Approach: Two-Pass Hash Map. Pass 1 counts the frequency of each value in the linked list. Pass 2 uses a dummy head to iterate and remove any node whose value appears more than once.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import Optional
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counts = Counter()
        curr = head
        while curr:
            counts[curr.val] += 1
            curr = curr.next

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if counts[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
