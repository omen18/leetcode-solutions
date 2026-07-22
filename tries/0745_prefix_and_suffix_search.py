"""
Problem: Prefix and Suffix Search
LeetCode #: 745
Difficulty: Hard
Link: https://leetcode.com/problems/prefix-and-suffix-search/

Approach: Insert transformed strings `suffix + '#' + prefix` into Trie. Query prefix + '#' + suffix in Trie.
Time Complexity: O(N * L^2) initialization, O(P + S) per query
Space Complexity: O(N * L^2) for Trie storage
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1


class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for weight, word in enumerate(words):
            l = len(word)
            for i in range(l + 1):
                suff = word[i:]
                combo = suff + '#' + word
                node = self.root
                node.weight = weight
                for char in combo:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    node.weight = weight

    def f(self, pref: str, suff: str) -> int:
        target = suff + '#' + pref
        node = self.root
        for char in target:
            if char not in node.children:
                return -1
            node = node.children[char]
        return node.weight
