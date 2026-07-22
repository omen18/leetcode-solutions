"""
Problem: Design Linked List
LeetCode #: 707
Difficulty: Medium
Link: https://leetcode.com/problems/design-linked-list/

Approach: Implement a doubly linked list with dummy head and dummy tail nodes to simplify edge cases. Maintain a size counter for O(1) size checks and fast traversal optimization.
Time Complexity: O(1) for addAtHead, addAtTail; O(N) for get, addAtIndex, deleteAtIndex.
Space Complexity: O(N) where N is the number of elements in the linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = DLLNode(0)
        self.tail = DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        # Traverse from head or tail depending on index
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0

        pred = self.head
        for _ in range(index):
            pred = pred.next
        succ = pred.next

        new_node = DLLNode(val, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        pred = self.head
        for _ in range(index):
            pred = pred.next
        succ = pred.next.next

        pred.next = succ
        succ.prev = pred
        self.size -= 1
