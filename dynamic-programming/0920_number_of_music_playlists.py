"""
Problem: Number of Music Playlists
LeetCode #: 920
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-music-playlists/

Approach: Dynamic Programming with space optimization.
`dp[j]` represents the number of playlists of length `i` containing `j` unique songs.
Transitions for step `i`:
1. Adding a new (unplayed) song: `dp[j-1] * (N - (j - 1))`
2. Replaying an already played song (valid if `j > K`): `dp[j] * (j - K)`
Time Complexity: O(goal * n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, goal + 1):
            next_dp = [0] * (n + 1)
            for j in range(1, min(i, n) + 1):
                # Case 1: Play a new song
                way1 = next_dp[j] = (dp[j - 1] * (n - (j - 1))) % MOD

                # Case 2: Replay an old song (must have played > k unique songs)
                way2 = 0
                if j > k:
                    way2 = (dp[j] * (j - k)) % MOD

                next_dp[j] = (way1 + way2) % MOD
            dp = next_dp

        return dp[n]
