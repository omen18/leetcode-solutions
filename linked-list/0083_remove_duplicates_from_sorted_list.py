"""
Problem: Remove Duplicates from Sorted List
LeetCode #: 83
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Approach: Iterate singly linked list and skip next node if current value equals next value.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1, ListNode(1, ListNode(2)))
    res = sol.deleteDuplicates(head)
    vals = []
    while res:
        vals.append(res.val)
        res = res.next
    print(vals)  # [1, 2]
