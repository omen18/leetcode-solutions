"""
Problem: Restore IP Addresses
LeetCode #: 93
Difficulty: Medium
Link: https://leetcode.com/problems/restore-ip-addresses/

Approach: Backtracking. Split string into 4 valid octets (each segment between 0 and 255 with no leading zeroes unless value is '0'). Track current segment count and string position.
Time Complexity: O(3^4) = O(1) constant bound.
Space Complexity: O(1) bounded recursion depth (4 segments).
"""

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def backtrack(start: int, segments: List[str]) -> None:
            if len(segments) == 4:
                if start == len(s):
                    result.append(".".join(segments))
                return
            
            for length in range(1, 4):
                if start + length > len(s):
                    break
                part = s[start:start + length]
                if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                    continue
                segments.append(part)
                backtrack(start + length, segments)
                segments.pop()
                
        backtrack(0, [])
        return result
