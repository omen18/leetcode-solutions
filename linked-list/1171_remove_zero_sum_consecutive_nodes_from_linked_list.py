"""
Problem: Remove Zero Sum Consecutive Nodes from Linked List
LeetCode #: 1171
Difficulty: Medium
Link: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

Approach: Use a prefix sum with a hash map mapping prefix sums to nodes. In the first pass, store the latest node associated with each prefix sum. In the second pass, set curr.next to prefix_map[prefix_sum].next to eliminate any sublist whose total sum is 0.
Time Complexity: O(N) where N is the number of nodes in the list.
Space Complexity: O(N) for storing prefix sums.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix_sum = 0
        prefix_map = {}

        # Pass 1: Calculate prefix sums and store the latest node for each prefix sum
        curr = dummy
        while curr:
            prefix_sum += curr.val
            prefix_map[prefix_sum] = curr
            curr = curr.next

        # Pass 2: Connect current node to the node after the last zero-sum sequence
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            curr.next = prefix_map[prefix_sum].next
            curr = curr.next

        return dummy.next
