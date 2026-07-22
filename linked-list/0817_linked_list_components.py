"""
Problem: Linked List Components
LeetCode #: 817
Difficulty: Medium
Link: https://leetcode.com/problems/linked-list-components/

Approach: Store values from nums in a set for O(1) lookups. Traverse the linked list and increment the component counter whenever a node's value is in nums_set and either it is the last node or its next node's value is NOT in nums_set.
Time Complexity: O(N + M) where N is list length and M is len(nums).
Space Complexity: O(M) for storing nums in a set.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        curr = head

        while curr:
            if curr.val in nums_set and (
                not curr.next or curr.next.val not in nums_set
            ):
                count += 1
            curr = curr.next

        return count
