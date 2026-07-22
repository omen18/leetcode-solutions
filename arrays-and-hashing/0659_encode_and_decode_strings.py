"""
Problem: Encode and Decode Strings
LeetCode #: 659
Difficulty: Medium
Link: https://leetcode.com/problems/encode-and-decode-strings/

Approach: Length-prefix encoding. Prepend each string with its length followed by a delimiter '#'.
Time Complexity: O(N) for both encode and decode where N is total number of characters across all strings.
Space Complexity: O(1) auxiliary space.
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
