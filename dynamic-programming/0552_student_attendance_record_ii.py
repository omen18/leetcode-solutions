"""
Problem: Student Attendance Record II
LeetCode #: 552
Difficulty: Hard
Link: https://leetcode.com/problems/student-attendance-record-ii/

Approach: State Dynamic Programming. Track 6 states defined by `(absences, consecutive_lates)`:
- `absences` in `{0, 1}`
- `consecutive_lates` in `{0, 1, 2}`
For each step from 1 to `n`, append 'P', 'L', or 'A' and update states modulo 10^9 + 7.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[a][l] = number of valid records with 'a' absences and ending with 'l' consecutive lates
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            next_dp = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    count = dp[a][l]
                    if count == 0:
                        continue

                    # Option 1: Append 'P' (resets late count to 0)
                    next_dp[a][0] = (next_dp[a][0] + count) % MOD

                    # Option 2: Append 'L' (increments late count if l < 2)
                    if l < 2:
                        next_dp[a][l + 1] = (next_dp[a][l + 1] + count) % MOD

                    # Option 3: Append 'A' (increments absence count if a < 1, resets late count to 0)
                    if a < 1:
                        next_dp[a + 1][0] = (next_dp[a + 1][0] + count) % MOD

            dp = next_dp

        res = 0
        for a in range(2):
            for l in range(3):
                res = (res + dp[a][l]) % MOD

        return res
