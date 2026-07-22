"""
Problem: Split Linked List in Parts
LeetCode #: 725
Difficulty: Medium
Link: https://leetcode.com/problems/split-linked-list-in-parts/

Approach: First count the total length N of the linked list. Each of the k parts will have size N // k, and the first N % k parts will get 1 extra node. Traverse the list to partition it into k sub-lists, disconnecting the end of each sub-list.
Time Complexity: O(N + k) where N is the number of nodes in the list.
Space Complexity: O(k) for storing the result list.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        # Count total length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        base_size, extra = divmod(length, k)

        res = []
        curr = head

        for i in range(k):
            part_head = curr
            part_size = base_size + (1 if i < extra else 0)

            for j in range(part_size - 1):
                if curr:
                    curr = curr.next

            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt

            res.append(part_head)

        return res
