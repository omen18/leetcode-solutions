"""
Problem: Concatenated Words
LeetCode #: 472
Difficulty: Hard
Link: https://leetcode.com/problems/concatenated-words/

Approach: Hash Set + Memoized Backtracking/DFS. Insert all words into a hash set. For each word, recursively check if it can be formed by concatenating 2 or more non-empty words from the set.
Time Complexity: O(N * L^2) where N is number of words and L is max length of a word.
Space Complexity: O(N * L) for hash set and memoization cache.
"""

from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}
        
        def can_form(word: str) -> bool:
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set:
                    if suffix in word_set or can_form(suffix):
                        memo[word] = True
                        return True
                    
            memo[word] = False
            return False
        
        result = []
        for word in words:
            if not word:
                continue
            if can_form(word):
                result.append(word)
                
        return result
