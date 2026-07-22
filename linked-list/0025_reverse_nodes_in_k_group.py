"""
Problem: Reverse Nodes in k-Group
LeetCode #: 25
Difficulty: Hard
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Approach: Iterate through the list, identifying sublists of size k. For each group of k nodes, reverse their pointers in-place and reconnect them with the preceding and succeeding parts of the linked list. If fewer than k nodes remain, leave them untouched.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1) extra space.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Check if there are at least k nodes left to reverse
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the k nodes in current group
            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Update connections
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
