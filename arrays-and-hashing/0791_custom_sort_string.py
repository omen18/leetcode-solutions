"""
Problem: Custom Sort String
LeetCode #: 791
Difficulty: Medium
Link: https://leetcode.com/problems/custom-sort-string/

Approach: Count frequencies of characters in s, append chars present in order first, then append remaining characters.
Time Complexity: O(N + M) where N is length of s and M is length of order.
Space Complexity: O(N) for frequency counter and result string construction.
"""

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []

        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]

        for char, freq in count.items():
            res.append(char * freq)

        return "".join(res)
