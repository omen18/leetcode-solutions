"""
Problem: Permutation Sequence
LeetCode #: 60
Difficulty: Hard
Link: https://leetcode.com/problems/permutation-sequence/

Approach: Factorial number system to pick digits index by index.
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1
        res = []
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            idx = k // fact
            res.append(numbers.pop(idx))
            k %= fact
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3, 3))  # "213"
