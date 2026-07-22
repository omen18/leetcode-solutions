"""
Problem: Largest Combination With Bitwise AND Greater Than Zero
LeetCode #: 2275
Difficulty: Medium
Link: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

Approach: Count the number of elements that have a '1' at each of the 30 bit positions and return the maximum count.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_size = 0
        for bit in range(30):
            count = sum((num >> bit) & 1 for num in candidates)
            if count > max_size:
                max_size = count
        return max_size
