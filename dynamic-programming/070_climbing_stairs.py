"""
Problem: Climbing Stairs
LeetCode #: 70
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

Approach: Dynamic programming — Fibonacci-like pattern.
          dp[i] = dp[i-1] + dp[i-2]
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))   # 2
    print(sol.climbStairs(3))   # 3
    print(sol.climbStairs(5))   # 8
