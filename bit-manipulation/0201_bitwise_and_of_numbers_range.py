"""
Problem: Bitwise AND of Numbers Range
LeetCode #: 201
Difficulty: Medium
Link: https://leetcode.com/problems/bitwise-and-of-numbers-range/

Approach: Find the common binary prefix of left and right boundaries by right-shifting until equality.
Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
