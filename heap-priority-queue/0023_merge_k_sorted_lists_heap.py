"""
Problem: Merge k Sorted Lists
LeetCode #: 23
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Approach: Min-heap storing tuples (node.val, index, node).
Push the head of each of the k non-empty linked lists into the min-heap.
Use the list index as a tie-breaker so Python doesn't attempt to compare ListNode instances directly.
Pop the smallest node from min-heap, attach to dummy result list, and if `node.next` exists, push `(node.next.val, index, node.next)`.

Time Complexity: O(N log k) where N is total number of nodes across all lists, k is number of linked lists
Space Complexity: O(k) for the heap
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
