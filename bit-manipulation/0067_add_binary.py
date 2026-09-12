"""
Problem: Add Binary
LeetCode #: 67
Difficulty: Easy
Link: https://leetcode.com/problems/add-binary/

Approach: Iterate backwards through binary strings with a carry bit.
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(res))


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))       # "100"
    print(sol.addBinary("1010", "1011"))  # "10101"
