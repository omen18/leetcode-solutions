"""
Problem: Break a Palindrome
LeetCode #: 1328
Difficulty: Medium
Link: https://leetcode.com/problems/break-a-palindrome/

Approach: If length <= 1, return "". Otherwise, replace first non-'a' character in the first half with 'a'. If all characters in the first half are 'a', replace the last character with 'b'.
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
            
        s = list(palindrome)
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return "".join(s)
                
        s[n - 1] = 'b'
        return "".join(s)
