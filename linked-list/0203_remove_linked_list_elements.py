"""
Problem: Remove Linked List Elements
LeetCode #: 203
Difficulty: Easy
Link: https://leetcode.com/problems/remove-linked-list-elements/

Approach: Use sentinel dummy node to easily remove target elements including head.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    h = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    res = sol.removeElements(h, 6)
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)  # [1, 2, 3, 4, 5]
