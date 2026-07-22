"""
Problem: Design Search Autocomplete System
LeetCode #: 642
Difficulty: Hard
Link: https://leetcode.com/problems/design-search-autocomplete-system/

Approach: Trie combined with sentence frequency counts. Traverse Trie as characters are input; on '#', save sentence and reset query.
Time Complexity: O(N * L) for initialization, O(L + M log 3) per input character where M is matching candidate count.
Space Complexity: O(N * L) for storing sentences in Trie.
"""

from collections import defaultdict
from typing import List


class TrieNode:

    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr_node = self.root
        self.curr_query = []

        for i in range(len(sentences)):
            self._insert(sentences[i], times[i])

    def _insert(self, sentence: str, count: int) -> None:
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences[sentence] += count

    def input(self, c: str) -> List[str]:
        if c == '#':
            sentence = "".join(self.curr_query)
            self._insert(sentence, 1)
            self.curr_query = []
            self.curr_node = self.root
            return []

        self.curr_query.append(c)

        if self.curr_node and c in self.curr_node.children:
            self.curr_node = self.curr_node.children[c]
            # Sort candidate sentences by frequency descending, then ascii order ascending
            candidates = sorted(
                self.curr_node.sentences.items(),
                key=lambda x: (-x[1], x[0]),
            )
            return [s for s, _ in candidates[:3]]
        else:
            self.curr_node = None
            return []
