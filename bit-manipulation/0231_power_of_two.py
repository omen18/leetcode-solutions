"""
Problem: Power of Two
LeetCode #: 231
Difficulty: Easy
Link: https://leetcode.com/problems/power-of-two/

Approach: A power of two has exactly one set bit: n > 0 and (n & (n - 1)) == 0.
Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPowerOfTwo(16))  # True
    print(sol.isPowerOfTwo(3))   # False
