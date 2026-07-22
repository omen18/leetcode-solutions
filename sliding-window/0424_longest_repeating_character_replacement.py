"""
Problem: Longest Repeating Character Replacement
LeetCode #: 424
Difficulty: Medium
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Approach: Sliding window with character frequency count. Maintain `max_freq` of any single character in window. If `window_length - max_freq > k`, shrink window from left.
Time Complexity: O(n)
Space Complexity: O(1) (26 uppercase letters)
"""

from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_freq = max(max_freq, counts[s[right]])

            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
