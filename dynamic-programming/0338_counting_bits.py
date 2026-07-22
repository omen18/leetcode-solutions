"""
Problem: Counting Bits
LeetCode #: 338
Difficulty: Easy
Link: https://leetcode.com/problems/counting-bits/

Approach: Dynamic Programming (Bit Manipulation) - Utilizing set bits relation ans[i] = ans[i >> 1] + (i & 1).
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
