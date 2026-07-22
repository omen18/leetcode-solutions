"""
Problem: Number of Dice Rolls With Target Sum
LeetCode #: 1155
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

Approach: Dynamic Programming with state compression. `dp[t]` stores number of ways to reach target sum `t`.
Iterate dice from 1 to `n`, updating `dp[t]` using the sum of reachable targets `dp[t - val]` for `1 <= val <= k`.
Time Complexity: O(n * target * k)
Space Complexity: O(target)
"""

from typing import List


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        if target < n or target > n * k:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1

        for dice in range(1, n + 1):
            next_dp = [0] * (target + 1)
            for t in range(dice, min(target, dice * k) + 1):
                for face in range(1, min(k, t) + 1):
                    next_dp[t] = (next_dp[t] + dp[t - face]) % MOD
            dp = next_dp

        return dp[target]
