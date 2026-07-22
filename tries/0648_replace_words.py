"""
Problem: Replace Words
LeetCode #: 648
Difficulty: Medium
Link: https://leetcode.com/problems/replace-words/

Approach: Insert dictionary roots into Trie. For each word in sentence, traverse Trie to find shortest root prefix.
Time Complexity: O(D * L + S * W) where D is dict size, L is word length, S is sentence words, W is avg word length
Space Complexity: O(D * L) for Trie storage
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for d_word in dictionary:
            node = root
            for char in d_word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = d_word

        words = sentence.split(" ")
        res = []
        for w in words:
            node = root
            replacement = w
            for char in w:
                if char not in node.children or node.word:
                    if node.word:
                        replacement = node.word
                    break
                node = node.children[char]
            if node.word:
                replacement = node.word
            res.append(replacement)

        return " ".join(res)
