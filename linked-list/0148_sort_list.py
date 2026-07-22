"""
Problem: Sort List
LeetCode #: 148
Difficulty: Medium
Link: https://leetcode.com/problems/sort-list/

Approach: Perform bottom-up or top-down Merge Sort on the linked list. Find the midpoint using slow/fast pointers, break the list into two halves, recursively sort both halves, and merge the sorted lists.
Time Complexity: O(N log N) where N is the number of nodes in the linked list.
Space Complexity: O(log N) due to recursive call stack.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves
        return self._merge(left, right)

    def _merge(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2
        return dummy.next
