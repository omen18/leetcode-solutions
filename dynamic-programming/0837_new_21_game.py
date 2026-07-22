"""
Problem: New 21 Game
LeetCode #: 837
Difficulty: Medium
Link: https://leetcode.com/problems/new-21-game/

Approach: Dynamic Programming with Sliding Window. `dp[i]` is the probability of having `i` points.
When total points are less than `k`, Alice draws a card from 1 to `maxPts` uniformly.
Maintain a sliding window sum of the last `maxPts` probabilities to update `dp[i]` efficiently.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return sum(dp[k:])
