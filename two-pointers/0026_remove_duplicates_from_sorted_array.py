"""
Problem: Remove Duplicates from Sorted Array
LeetCode #: 26
Difficulty: Easy
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Approach: Two pointers: keep index k for unique elements and iterate through array.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # 2, [1, 2]
