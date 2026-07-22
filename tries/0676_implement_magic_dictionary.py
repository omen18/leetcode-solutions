"""
Problem: Implement Magic Dictionary
LeetCode #: 676
Difficulty: Medium
Link: https://leetcode.com/problems/implement-magic-dictionary/

Approach: Build Trie from dictionary words. DFS search allows exactly one character mismatch.
Time Complexity: buildDict: O(N * L), search: O(26 * L)
Space Complexity: O(N * L) for Trie storage
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True

    def search(self, searchWord: str) -> bool:
        def dfs(node: TrieNode, i: int, modified: bool) -> bool:
            if i == len(searchWord):
                return node.is_end and modified

            char = searchWord[i]
            for child_char, child_node in node.children.items():
                if child_char == char:
                    if dfs(child_node, i + 1, modified):
                        return True
                elif not modified:
                    if dfs(child_node, i + 1, True):
                        return True
            return False

        return dfs(self.root, 0, False)
