"""
Problem: Swap Nodes in Pairs
LeetCode #: 24
Difficulty: Medium
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Approach: Iterate through the list using a dummy node and a pointer to the node preceding the current pair. Swap pair nodes in-place by updating pointer references.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second

            # Move pointer forward for next pair
            prev = first

        return dummy.next
