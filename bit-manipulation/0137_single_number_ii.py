"""
Problem: Single Number II
LeetCode #: 137
Difficulty: Medium
Link: https://leetcode.com/problems/single-number-ii/

Approach: Bitwise state machine (ones, twos) tracking occurrences modulo 3.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        # Handle 32-bit signed integer representation in Python
        if ones >= (1 << 31):
            ones -= 1 << 32

        return ones
