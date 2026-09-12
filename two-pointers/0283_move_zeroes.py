"""
Problem: Move Zeroes
LeetCode #: 283
Difficulty: Easy
Link: https://leetcode.com/problems/move-zeroes/

Approach: Two pointers swapping non-zero elements into position.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1


if __name__ == "__main__":
    sol = Solution()
    a = [0, 1, 0, 3, 12]
    sol.moveZeroes(a)
    print(a)  # [1, 3, 12, 0, 0]
