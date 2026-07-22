"""
Problem: Smallest Good Base
LeetCode #: 483
Difficulty: Hard
Link: https://leetcode.com/problems/smallest-good-base/

Approach: Binary search base k for polynomial length m = 60 down to 2 such that (k^m - 1) / (k - 1) = n.
Time Complexity: O((log N)^2)
Space Complexity: O(1)
"""


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        # m is the number of 1s in base k representation
        # Maximum m is 63 since 2^63 > 10^18
        for m in range(63, 1, -1):
            # Estimate base k using integer root approximation
            k = int(num ** (1 / (m - 1)))
            if k > 1:
                # Calculate polynomial sum 1 + k + k^2 + ... + k^(m-1)
                val = 0
                for _ in range(m):
                    val = val * k + 1

                if val == num:
                    return str(k)

        return str(num - 1)
