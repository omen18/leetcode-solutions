"""
Problem: Dungeon Game
LeetCode #: 174
Difficulty: Hard
Link: https://leetcode.com/problems/dungeon-game/

Approach: Bottom-up 2D dynamic programming working backwards from princess room.
Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, min_health)
        return dp[0][0]


if __name__ == "__main__":
    sol = Solution()
    d = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(sol.calculateMinimumHP(d))  # 7
