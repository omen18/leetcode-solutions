"""
Problem: Find Minimum in Rotated Sorted Array II
LeetCode #: 154
Difficulty: Hard
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Approach: Binary search with high decrements when mid equals high.
Time Complexity: O(log n) average, O(n) worst case
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        return nums[low]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([2, 2, 2, 0, 1]))  # 0
