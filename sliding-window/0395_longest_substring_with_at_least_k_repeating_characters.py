"""
Problem: Longest Substring with At Least K Repeating Characters
LeetCode #: 395
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Approach: Divide and Conquer. Count character frequencies in current string. If any character appears fewer than k times, any valid substring cannot contain it. Split the string by this invalid character and recurse on each segment.
Time Complexity: O(N)
Space Complexity: O(N) recursive stack depth
"""

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        counts = Counter(s)
        for char, count in counts.items():
            if count < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(char))

        return len(s)
