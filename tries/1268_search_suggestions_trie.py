"""
Problem: Search Suggestions System
LeetCode #: 1268
Difficulty: Medium
Link: https://leetcode.com/problems/search-suggestions-system/

Approach: Trie storing top 3 lexicographical words at each node. Products are sorted first.
Time Complexity: O(N log N + N * L + M) where N is products count, L is product length, M is searchWord length
Space Complexity: O(N * L) for Trie storage
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()

        for prod in products:
            node = root
            for char in prod:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(prod)

        res = []
        node = root
        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                res.append(node.suggestions)
            else:
                node = None
                res.append([])

        return res
