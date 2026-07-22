"""
Problem: Non-negative Integers without Consecutive Ones
LeetCode #: 600
Difficulty: Hard
Link: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

Approach: Digit Dynamic Programming using Fibonacci numbers.
Precalculate Fibonacci numbers `f[i]` where `f[i]` represents number of valid binary strings of length `i`
without consecutive ones (`f[0]=1, f[1]=2, f[2]=3, ...`).
Iterate bits of `n` from MSB to LSB. When a bit is 1, add `f[bit]` to result.
If two consecutive 1 bits are encountered, break early as higher constraints are violated.
Time Complexity: O(log N)
Space Complexity: O(log N)
"""

from typing import List


class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0] = 1
        f[1] = 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]

        ans = 0
        prev_bit = 0
        bin_str = bin(n)[2:]
        k = len(bin_str)

        for i in range(k):
            if bin_str[i] == '1':
                ans += f[k - 1 - i]
                if prev_bit == 1:
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0

        return ans + 1
