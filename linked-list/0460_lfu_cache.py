"""
Problem: LFU Cache
LeetCode #: 460
Difficulty: Hard
Link: https://leetcode.com/problems/lfu-cache/

Approach: Maintain a key-to-node hash map, a freq-to-doubly-linked-list hash map, and a min_freq counter. Each frequency key maps to a doubly linked list storing nodes with that access frequency in LRU order.
Time Complexity: O(1) for both get and put operations.
Space Complexity: O(capacity) for storing nodes across hash maps and frequency lists.
"""

from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self) -> Optional[Node]:
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.freq_to_dll = defaultdict(DoublyLinkedList)
        self.min_freq = 0

    def _update_freq(self, node: Node) -> None:
        freq = node.freq
        self.freq_to_dll[freq].remove(node)

        if self.freq_to_dll[freq].size == 0 and self.min_freq == freq:
            self.min_freq += 1

        node.freq += 1
        self.freq_to_dll[node.freq].add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                lfu_dll = self.freq_to_dll[self.min_freq]
                removed_node = lfu_dll.remove_tail()
                if removed_node:
                    del self.key_to_node[removed_node.key]

            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.freq_to_dll[1].add_to_head(new_node)
            self.min_freq = 1
