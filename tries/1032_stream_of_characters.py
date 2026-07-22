"""
Problem: Stream of Characters
LeetCode #: 1032
Difficulty: Hard
Link: https://leetcode.com/problems/stream-of-characters/

Approach: Insert reversed words into Trie. On each stream query character, prepend character to running stream history and search in Trie.
Time Complexity: O(W * L) initialization; O(L) per query where L is max word length
Space Complexity: O(W * L) for Trie + O(L) for stream history
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.history = []
        self.max_len = 0

        for word in words:
            self.max_len = max(self.max_len, len(word))
            node = self.root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        node = self.root
        for char in reversed(self.history):
            if char not in node.children:
                return False
            node = node.children[char]
            if node.is_end:
                return True
        return False
