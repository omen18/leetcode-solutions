"""
Problem: String to Integer (atoi)
LeetCode #: 8
Difficulty: Medium
Link: https://leetcode.com/problems/string-to-integer-atoi/

Approach: Strip leading whitespace, determine sign, convert consecutive digits, and clamp to 32-bit bounds.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == "-":
            sign = -1
            i = 1
        elif s[0] == "+":
            i = 1
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))          # 42
    print(sol.myAtoi("   -042"))     # -42
    print(sol.myAtoi("1337c0d3"))    # 1337
