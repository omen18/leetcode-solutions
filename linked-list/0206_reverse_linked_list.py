"""
Problem: Reverse Linked List
LeetCode #: 206
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

Approach: Iterative pointer reversal tracking prev and curr nodes.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == "__main__":
    sol = Solution()
    h = ListNode(1, ListNode(2, ListNode(3)))
    res = sol.reverseList(h)
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)  # [3, 2, 1]
