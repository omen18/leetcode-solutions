"""
Problem: Gray Code
LeetCode #: 89
Difficulty: Medium
Link: https://leetcode.com/problems/gray-code/

Approach: Generate i ^ (i >> 1) for each index in 0..2^n - 1.
Time Complexity: O(2^n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(2))  # [0, 1, 3, 2]
