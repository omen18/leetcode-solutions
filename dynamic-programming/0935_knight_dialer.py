"""
Problem: Knight Dialer
LeetCode #: 935
Difficulty: Medium
Link: https://leetcode.com/problems/knight-dialer/

Approach: Dynamic Programming. Define knight move transitions for each key 0-9.
Maintain a array `dp` of size 10 where `dp[i]` is the number of ways to reach key `i` in `step` moves.
Update `dp` array `n - 1` times and take sum modulo 10^9 + 7.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        dp = [1] * 10
        for _ in range(n - 1):
            next_dp = [0] * 10
            for digit in range(10):
                for prev in moves[digit]:
                    next_dp[digit] = (next_dp[digit] + dp[prev]) % MOD
            dp = next_dp

        return sum(dp) % MOD
