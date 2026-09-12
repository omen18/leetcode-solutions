"""
Problem: Power of Four
LeetCode #: 342
Difficulty: Easy
Link: https://leetcode.com/problems/power-of-four/

Approach: Power of two whose single set bit lies at an odd bit position (0x55555555 mask).
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfFour(16))  # True
    print(sol.isPowerOfFour(5))   # False
