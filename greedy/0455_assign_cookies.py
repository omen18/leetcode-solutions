"""
Problem: Assign Cookies
LeetCode #: 455
Difficulty: Medium
Link: https://leetcode.com/problems/assign-cookies/

Approach: Sort children's greed and cookie sizes. Use two pointers to assign the smallest cookie that satisfies each child.
Time Complexity: O(N log N + M log M)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0
        j = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
            
        return i
