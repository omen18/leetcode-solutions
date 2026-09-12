"""
Problem: Reverse Integer
LeetCode #: 7
Difficulty: Medium
Link: https://leetcode.com/problems/reverse-integer/

Approach: Extract digits from the right, build reversed integer, and check for 32-bit signed overflow.
Time Complexity: O(log |x|)
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        rev *= sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))   # 321
    print(sol.reverse(-123))  # -321
    print(sol.reverse(120))   # 21
