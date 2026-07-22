"""
Problem: Maximum Twin Sum of a Linked List
LeetCode #: 2130
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

Approach: 
1. Use fast and slow pointers to find the middle of the even-length linked list.
2. Reverse the second half of the linked list in-place.
3. Simultaneously traverse the first half and the reversed second half, calculating twin sums and updating the maximum sum observed.
Time Complexity: O(N) where N is the number of nodes in the linked list.
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        # Step 1: Find middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half starting at slow
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compute maximum twin sum
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum
