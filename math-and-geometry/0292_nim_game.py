"""
Problem: Nim Game
LeetCode #: 292
Difficulty: Easy
Link: https://leetcode.com/problems/nim-game/

Approach: Player loses if and only if pile count is a multiple of 4.
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.canWinNim(4))  # False
    print(sol.canWinNim(1))  # True
