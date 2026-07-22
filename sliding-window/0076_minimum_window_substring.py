"""
Problem: Minimum Window Substring
LeetCode #: 76
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/

Approach: Sliding window using character frequency counts. Expand `right` until window has all characters from `t` with needed frequencies. Then contract `left` while condition holds to minimize length.
Time Complexity: O(m + n) where m = len(s), n = len(t)
Space Complexity: O(m + n)
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_count = Counter(t)
        required = len(target_count)

        left, right = 0, 0
        formed = 0
        window_counts = Counter()

        ans = (float('inf'), 0, 0)  # (window length, left, right)

        while right < len(s):
            character = s[right]
            window_counts[character] += 1

            if character in target_count and window_counts[character] == target_count[character]:
                formed += 1

            while left <= right and formed == required:
                character = s[left]

                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_counts[character] -= 1
                if character in target_count and window_counts[character] < target_count[character]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]
