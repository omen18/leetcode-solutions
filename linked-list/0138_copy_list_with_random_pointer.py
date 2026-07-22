"""
Problem: Copy List with Random Pointer
LeetCode #: 138
Difficulty: Medium
Link: https://leetcode.com/problems/copy-list-with-random-pointer/

Approach: Use a hash map mapping original nodes to their cloned node counterparts. In the first pass, create all cloned nodes without pointer links. In the second pass, assign the next and random pointers for each cloned node using the hash map.
Time Complexity: O(N) where N is the number of nodes.
Space Complexity: O(N) for storing original-to-clone node mappings.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # First pass: create all cloned nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: wire up next and random pointers
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]
