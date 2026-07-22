"""
Problem: Design Add and Search Words Data Structure
LeetCode #: 211
Difficulty: Medium
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Approach: Trie with DFS backtracking for wildcard '.' search.
Time Complexity: O(N) for addWord; O(N) for search without '.', up to O(26^N) worst-case with '.'
Space Complexity: O(T) total characters stored
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.is_end

        return dfs(0, self.root)
