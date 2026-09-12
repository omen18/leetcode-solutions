"""
Problem: Next Permutation
LeetCode #: 31
Difficulty: Medium
Link: https://leetcode.com/problems/next-permutation/

Approach: Find first decreasing element from right, swap with next greater, and reverse suffix.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == "__main__":
    sol = Solution()
    a = [1, 2, 3]
    sol.nextPermutation(a)
    print(a)  # [1, 3, 2]
