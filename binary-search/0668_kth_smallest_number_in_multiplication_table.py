"""
Problem: Kth Smallest Number in Multiplication Table
LeetCode #: 668
Difficulty: Hard
Link: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

Approach: Binary search on value x in range [1, m * n]. Count numbers <= x in the table using sum(min(x // i, n) for i in range(1, m + 1)). Find smallest x with count >= k.
Time Complexity: O(m * log(m * n))
Space Complexity: O(1)
"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n

        while left < right:
            mid = (left + right) // 2
            count = sum(min(mid // i, n) for i in range(1, m + 1))

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
