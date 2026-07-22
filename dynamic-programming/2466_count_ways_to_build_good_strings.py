"""
Problem: Count Ways To Build Good Strings
LeetCode #: 2466
Difficulty: Medium
Link: https://leetcode.com/problems/count-ways-to-build-good-strings/

Approach: Dynamic Programming. `dp[i]` stores the number of valid strings of length `i`.
Transition: `dp[i] = (dp[i - zero] + dp[i - one]) % MOD`.
Sum up `dp[i]` for all lengths `i` from `low` to `high`.
Time Complexity: O(high)
Space Complexity: O(high)
"""

from typing import List


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD

        return sum(dp[low:high + 1]) % MOD
