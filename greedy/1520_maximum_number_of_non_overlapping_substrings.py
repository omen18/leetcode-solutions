"""
Problem: Maximum Number of Non-Overlapping Substrings
LeetCode #: 1520
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

Approach: Determine valid substrings for each character by expanding bounds to cover all occurrences of internal characters. Sort valid intervals by end position and select non-overlapping intervals greedily.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        intervals = []
        for ch in first:
            start = first[ch]
            end = last[ch]
            i = start
            valid = True
            while i <= end:
                c = s[i]
                if first[c] < start:
                    valid = False
                    break
                end = max(end, last[c])
                i += 1
            if valid:
                intervals.append((start, end))
                
        intervals.sort(key=lambda x: x[1])
        
        res = []
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                res.append(s[start:end + 1])
                last_end = end
                
        return res
