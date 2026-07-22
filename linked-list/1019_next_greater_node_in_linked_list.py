"""
Problem: Next Greater Node In Linked List
LeetCode #: 1019
Difficulty: Medium
Link: https://leetcode.com/problems/next-greater-node-in-linked-list/

Approach: Convert the linked list into an array of values. Use a monotonic decreasing stack to efficiently find the next strictly greater value for each element.
Time Complexity: O(N) where N is the number of nodes in the list.
Space Complexity: O(N) for storing values and the stack.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        res = [0] * len(vals)
        stack = []  # Store indices

        for i, val in enumerate(vals):
            while stack and vals[stack[-1]] < val:
                idx = stack.pop()
                res[idx] = val
            stack.append(i)

        return res
