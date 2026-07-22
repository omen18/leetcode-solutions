"""
Problem: Longest Word in Dictionary
LeetCode #: 720
Difficulty: Medium
Link: https://leetcode.com/problems/longest-word-in-dictionary/

Approach: Sort words lexicographically and build a Set/Trie, verifying each word can be built one character at a time.
Time Complexity: O(N * L + N log N) where N is number of words, L is max word length
Space Complexity: O(N * L)
"""

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        built = set([""])
        longest = ""

        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(longest):
                    longest = word

        return longest
