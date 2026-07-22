"""
Problem: Palindrome Pairs
LeetCode #: 336
Difficulty: Hard
Link: https://leetcode.com/problems/palindrome-pairs/

Approach: HashMap lookup for matching reversed prefixes/suffixes. For each word, check prefix and suffix splits for palindrome properties.
Time Complexity: O(N * K^2) where N is number of words and K is max word length
Space Complexity: O(N * K)
"""

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_idx = {word: i for i, word in enumerate(words)}
        res = []

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                pref = word[:j]
                suff = word[j:]

                if is_palindrome(pref):
                    back = suff[::-1]
                    if back in word_to_idx and word_to_idx[back] != i:
                        res.append([word_to_idx[back], i])

                if j < n and is_palindrome(suff):
                    back = pref[::-1]
                    if back in word_to_idx and word_to_idx[back] != i:
                        res.append([i, word_to_idx[back]])

        return res
