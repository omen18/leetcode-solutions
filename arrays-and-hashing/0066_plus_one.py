"""
Problem: Plus One
LeetCode #: 66
Difficulty: Easy
Link: https://leetcode.com/problems/plus-one/

Approach: Iterate backwards adding carry; prepend 1 if most significant digit overflows.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(sol.plusOne([9, 9, 9]))  # [1, 0, 0, 0]
