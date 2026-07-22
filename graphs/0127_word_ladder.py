"""
Problem: Word Ladder
LeetCode #: 127
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/

Approach: BFS with Wildcard Pattern Indexing.
Map words to intermediate pattern keys with single character wildcards ('*').
Perform BFS starting from `beginWord` to find the shortest sequence length reaching `endWord`.

Time Complexity: O(N * L^2) where N is number of words and L is length of each word.
Space Complexity: O(N * L^2) for storing intermediate pattern dictionary and BFS queue.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1 :]
                all_combo_dict[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]

                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                all_combo_dict[pattern] = []

        return 0
