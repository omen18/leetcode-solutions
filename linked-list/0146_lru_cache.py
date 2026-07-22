"""
Problem: LRU Cache
LeetCode #: 146
Difficulty: Hard
Link: https://leetcode.com/problems/lru-cache/

Approach: Combine a hash map with a doubly linked list. The hash map provides O(1) key lookups, while the doubly linked list maintains the usage ordering of items. The Most Recently Used (MRU) items are kept near the head, and the Least Recently Used (LRU) items are kept near the tail.
Time Complexity: O(1) for both get and put operations.
Space Complexity: O(capacity) for storing nodes in the hash map and doubly linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DLLNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode

        # Dummy head (MRU side) and dummy tail (LRU side)
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode) -> None:
        """Remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: DLLNode) -> None:
        """Insert node right after dummy head (most recently used position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict LRU item (node right before dummy tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
