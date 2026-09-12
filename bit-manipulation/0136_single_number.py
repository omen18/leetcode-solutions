"""
Problem: Single Number
LeetCode #: 136
Difficulty: Easy
Link: https://leetcode.com/problems/single-number/

Approach: XOR all elements together. Identical pairs cancel out (a ^ a = 0).
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))        # 1
    print(sol.singleNumber([4, 1, 2, 1, 2]))  # 4
