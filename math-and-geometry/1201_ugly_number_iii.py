"""
Problem: Ugly Number III
LeetCode #: 1201
Difficulty: Medium
Link: https://leetcode.com/problems/ugly-number-iii/

Approach: Binary search the answer using the Inclusion-Exclusion Principle with LCMs.
Time Complexity: O(log(2 * 10^9))
Space Complexity: O(1)
"""

import math


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = math.lcm(a, b)
        bc = math.lcm(b, c)
        ac = math.lcm(a, c)
        abc = math.lcm(ab, c)

        def count(x: int) -> int:
            return (
                x // a
                + x // b
                + x // c
                - x // ab
                - x // bc
                - x // ac
                + x // abc
            )

        left, right = 1, 2 * 10**9
        res = right

        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= n:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
