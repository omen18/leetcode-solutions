"""
Problem: Linked List Cycle
LeetCode #: 141
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/

Approach: Floyd's Tortoise and Hare two-pointer cycle detection.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    print(sol.hasCycle(n1))  # True
