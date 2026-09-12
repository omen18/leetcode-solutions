"""
Problem: Range Sum Query - Immutable
LeetCode #: 303
Difficulty: Easy
Link: https://leetcode.com/problems/range-sum-query-immutable/

Approach: Prefix sum array where range sum = prefix[right + 1] - prefix[left].
Time Complexity: Constructor O(n), Query O(1)
Space Complexity: O(n)
"""

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sumRange(0, 2))  # 1
    print(na.sumRange(2, 5))  # -1
