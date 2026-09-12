"""
Problem: Bulls and Cows
LeetCode #: 299
Difficulty: Medium
Link: https://leetcode.com/problems/bulls-and-cows/

Approach: One-pass counting matching positions (bulls) and frequency array (cows).
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        s_count, g_count = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[int(s)] += 1
                g_count[int(g)] += 1
        for i in range(10):
            cows += min(s_count[i], g_count[i])
        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    sol = Solution()
    print(sol.getHint("1807", "7810"))  # "1A3B"
