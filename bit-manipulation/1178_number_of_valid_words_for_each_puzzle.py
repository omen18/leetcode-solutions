"""
Problem: Number of Valid Words for Each Puzzle
LeetCode #: 1178
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

Approach: Represent words as 26-bit masks in a frequency map. For each puzzle, iterate over all 2^6 sub-bitmasks of its 6 non-first letters combined with its required first letter.
Time Complexity: O(W * L + P * 2^6) where W is len(words), P is len(puzzles), L is max word length.
Space Complexity: O(W)
"""

from collections import Counter
from typing import List


class Solution:
    def findNumOfValidWords(
        self, words: List[str], puzzles: List[str]
    ) -> List[int]:
        word_counts = Counter()

        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord("a"))
            # Only count words with <= 7 unique characters (matches puzzle constraint)
            if bin(mask).count("1") <= 7:
                word_counts[mask] += 1

        result = []

        for puzzle in puzzles:
            first_bit = 1 << (ord(puzzle[0]) - ord("a"))
            rest_mask = 0
            for char in puzzle[1:]:
                rest_mask |= 1 << (ord(char) - ord("a"))

            count = 0
            # Iterate through all sub-masks of rest_mask
            sub = rest_mask
            while True:
                full_mask = first_bit | sub
                count += word_counts[full_mask]

                if sub == 0:
                    break
                sub = (sub - 1) & rest_mask

            result.append(count)

        return result
