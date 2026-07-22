"""
Problem: Longest Word in Dictionary through Deleting
LeetCode #: 524
Difficulty: Medium
Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Approach: Sort dictionary by word length descending, then lexicographically ascending. For each word, check if it is a subsequence of `s` using two pointers.
Time Complexity: O(n * log(n) * w + n * |s|) where n = len(dictionary), w = max word length
Space Complexity: O(1) auxiliary (excluding sorting)
"""

from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda word: (-len(word), word))

        for word in dictionary:
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
            if i == len(word):
                return word

        return ""
