"""
Problem: Decode Ways
LeetCode #: 91
Difficulty: Medium
Link: https://leetcode.com/problems/decode-ways/

Approach: Dynamic programming using constant space to track decodings up to 1-digit and 2-digit valid numbers.
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        prev2, prev1 = 1, 1
        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr += prev1
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr
            
        return prev1
