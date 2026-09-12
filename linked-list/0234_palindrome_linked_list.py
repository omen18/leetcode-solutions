"""
Problem: Palindrome Linked List
LeetCode #: 234
Difficulty: Easy
Link: https://leetcode.com/problems/palindrome-linked-list/

Approach: Find midpoint with fast/slow pointers, reverse second half, compare values.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


if __name__ == "__main__":
    sol = Solution()
    h = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(sol.isPalindrome(h))  # True
