"""
Problem: Multiply Strings
LeetCode #: 43
Difficulty: Medium
Link: https://leetcode.com/problems/multiply-strings/

Approach: Elementary grade-school multiplication digit-by-digit into a result array of size len(num1) + len(num2). Propagate carries and format as string.
Time Complexity: O(m * n) where m and n are string lengths.
Space Complexity: O(m + n)
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        # Find first non-zero digit
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return "".join(map(str, res[start:]))
