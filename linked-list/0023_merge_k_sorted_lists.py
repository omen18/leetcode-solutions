"""
Problem: Merge k Sorted Lists
LeetCode #: 23
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Approach: Maintain a min-heap storing tuples of (node.val, index, node) for the head of each non-empty linked list. Repeatedly extract the minimum node, append it to the result list, and push its next node (if any) into the min-heap.
Time Complexity: O(N log k) where N is the total number of nodes across all k lists.
Space Complexity: O(k) for storing the min-heap elements.
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        heap = []

        # Push the head of each list into the heap with its index to break ties
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
