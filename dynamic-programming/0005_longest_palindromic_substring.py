"""
Problem: Longest Palindromic Substring
LeetCode #: 5
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/

Approach: Expand around center for each index (both odd and even length centers).
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, max_len = 0, 0
        
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            length = max(len1, len2)
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2
                
        return s[start:start + max_len]
