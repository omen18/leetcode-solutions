"""
Problem: Jump Game VII
LeetCode #: 1871
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game-vii/

Approach: Dynamic Programming with Sliding Window / Running sum of reachable states.
`dp[i]` is True if index `i` is reachable and `s[i] == '0'`.
Maintain `reachable_count` of valid indices in the window `[i - maxJump, i - minJump]`.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] != '0':
            return False

        dp = [False] * n
        dp[0] = True
        reachable_count = 0

        for i in range(1, n):
            if i >= minJump and dp[i - minJump]:
                reachable_count += 1
            if i > maxJump and dp[i - maxJump - 1]:
                reachable_count -= 1

            if s[i] == '0' and reachable_count > 0:
                dp[i] = True

        return dp[n - 1]
