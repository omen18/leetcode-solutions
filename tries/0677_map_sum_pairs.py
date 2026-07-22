"""
Problem: Map Sum Pairs
LeetCode #: 677
Difficulty: Medium
Link: https://leetcode.com/problems/map-sum-pairs/

Approach: Trie where each node tracks the sum of values for all words passing through it.
Track word values in a hash map to handle key overwrites by updating delta (val - prev_val).
Time Complexity: O(K) for insert and sum, where K is length of key/prefix
Space Complexity: O(N * K) for storing keys in Trie
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.value_sum = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        node = self.root
        node.value_sum += delta
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.value_sum += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value_sum
