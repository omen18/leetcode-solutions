"""
Problem: H-Index
LeetCode #: 274
Difficulty: Medium
Link: https://leetcode.com/problems/h-index/

Approach: Counting sort / bucket sort approach. Count papers for each citation count up to n (where counts >= n are stored at index n). Iterate backwards to find the maximum h.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1

        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i

        return 0
