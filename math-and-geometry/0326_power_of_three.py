"""
Problem: Power of Three
LeetCode #: 326
Difficulty: Easy
Link: https://leetcode.com/problems/power-of-three/

Approach: Check divisibility by largest 32-bit integer power of 3 (1162261467).
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfThree(27))  # True
    print(sol.isPowerOfThree(0))   # False
