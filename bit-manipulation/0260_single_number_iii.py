"""
Problem: Single Number III
LeetCode #: 260
Difficulty: Medium
Link: https://leetcode.com/problems/single-number-iii/

Approach: Find overall XOR sum, isolate lowest set bit to partition numbers into two groups, and XOR each group.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num

        # Isolate lowest set bit
        diff_bit = xor_sum & -xor_sum

        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
