"""
Problem: Best Team With No Conflicts
LeetCode #: 1626
Difficulty: Medium
Link: https://leetcode.com/problems/best-team-with-no-conflicts/

Approach: Dynamic Programming (LIS variation). Sort players primarily by age and secondarily by score.
After sorting, age constraints are automatically preserved (`age[i] <= age[j]` for `i < j`), so we need to find
a subsequence of scores that is non-decreasing to avoid conflicts. `dp[i]` stores max score ending at player `i`.
Time Complexity: O(N^2)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        n = len(players)
        dp = [p[1] for p in players]

        for i in range(n):
            for j in range(i):
                if players[j][1] <= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)
