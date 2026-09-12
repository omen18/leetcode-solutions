"""
Problem: Intersection of Two Linked Lists
LeetCode #: 160
Difficulty: Easy
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Approach: Two pointers: switch to opposite list head upon reaching None to equalize paths.
Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = headB if not pA else pA.next
            pB = headA if not pB else pB.next
        return pA


if __name__ == "__main__":
    sol = Solution()
    common = ListNode(8)
    l1 = ListNode(4)
    l1.next = common
    l2 = ListNode(5)
    l2.next = common
    print(sol.getIntersectionNode(l1, l2).val)  # 8
