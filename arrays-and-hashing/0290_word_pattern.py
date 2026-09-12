"""
Problem: Word Pattern
LeetCode #: 290
Difficulty: Easy
Link: https://leetcode.com/problems/word-pattern/

Approach: Bijection check with two hash maps between characters and words.
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word, word_to_char = {}, {}
        for c, w in zip(pattern, words):
            if (c in char_to_word and char_to_word[c] != w) or (w in word_to_char and word_to_char[w] != c):
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))  # True
    print(sol.wordPattern("abba", "dog cat cat fish")) # False
