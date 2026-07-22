"""
Problem: Solving Questions With Brainpower
LeetCode #: 2140
Difficulty: Medium
Link: https://leetcode.com/problems/solving-questions-with-brainpower/

Approach: Dynamic Programming (Backward pass). `dp[i]` represents the max points earned from question `i` to the end.
For question `i` with points `p` and brainpower `b`:
Option 1: Skip question `i` -> `dp[i + 1]`
Option 2: Solve question `i` -> `p + dp[i + b + 1]` (if `i + b + 1 < n`)
`dp[i] = max(Option 1, Option 2)`.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_idx = i + brainpower + 1
            solve = points + (dp[next_idx] if next_idx < n else 0)
            skip = dp[i + 1]
            dp[i] = max(solve, skip)

        return dp[0]
