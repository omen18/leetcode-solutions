"""
Problem: Find All Anagrams in a String
LeetCode #: 438
Difficulty: Medium
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Approach: Sliding window of size len(p) maintaining character count frequency arrays.
Time Complexity: O(N) where N is length of string s.
Space Complexity: O(1) since character count array size is fixed at 26.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        s_count = [0] * 26

        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            s_count[ord(s[i]) - ord('a')] += 1

        res = []
        if s_count == p_count:
            res.append(0)

        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            if s_count == p_count:
                res.append(i - len(p) + 1)

        return res
