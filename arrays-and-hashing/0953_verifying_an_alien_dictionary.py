"""
Problem: Verifying an Alien Dictionary
LeetCode #: 953
Difficulty: Easy
Link: https://leetcode.com/problems/verifying-an-alien-dictionary/

Approach: Create a mapping of characters to their rank in the alien order. Compare adjacent word pairs character by character. If a mismatch occurs, check if the relative order is maintained.
Time Complexity: O(N) where N is total characters across all words.
Space Complexity: O(1) as alphabet size is fixed to 26.
"""

from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {char: i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True
