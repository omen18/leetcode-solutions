"""
Problem: Missing Number
LeetCode #: 268
Difficulty: Easy
Link: https://leetcode.com/problems/missing-number/

Approach: XOR all indices 0..n with array numbers to find the missing value.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))  # 2
