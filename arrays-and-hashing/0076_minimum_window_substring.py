"""
Problem: Minimum Window Substring
LeetCode #: 76
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/

Approach: Sliding window using character frequency counters. Track number of satisfied unique character conditions.
Time Complexity: O(N + M) where N is length of s and M is length of t.
Space Complexity: O(K) where K is number of unique characters in s and t (O(1) ASCII).
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_count = Counter(t)
        need = len(target_count)
        have = 0

        window = {}
        res = (-1, -1)
        min_len = float("inf")

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in target_count and window[char] == target_count[char]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = (l, r)

                window[s[l]] -= 1
                if s[l] in target_count and window[s[l]] < target_count[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if min_len != float("inf") else ""
