"""
Problem: Palindromic Substrings
LeetCode #: 647
Difficulty: Medium
Link: https://leetcode.com/problems/palindromic-substrings/

Approach: Expand around center algorithm counting palindromes formed around odd/even centers.
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def expand(left: int, right: int) -> int:
            cnt = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt
            
        for i in range(len(s)):
            count += expand(i, i)      # Odd length
            count += expand(i, i + 1)  # Even length
            
        return count
