"""
Problem: Merge Two Sorted Lists
LeetCode #: 21
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Approach: Use a dummy head and iterate while both lists have nodes, splicing the smaller value node next.
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = sol.mergeTwoLists(l1, l2)
    res = []
    while merged:
        res.append(merged.val)
        merged = merged.next
    print(res)  # [1, 1, 2, 3, 4, 4]
