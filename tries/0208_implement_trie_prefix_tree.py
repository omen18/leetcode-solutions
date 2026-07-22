"""
Problem: Implement Trie (Prefix Tree)
LeetCode #: 208
Difficulty: Medium
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Approach: Trie structure using dictionary nodes where each node contains child nodes and an is_end flag.
Time Complexity: O(N) per operation where N is the length of the string
Space Complexity: O(T * C) where T is total characters inserted and C is alphabet size
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
