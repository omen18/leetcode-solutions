"""
Problem: Search Insert Position
LeetCode #: 35
Difficulty: Easy
Link: https://leetcode.com/problems/search-insert-position/

Approach: Binary search: find exact match or lower bound insertion point.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))  # 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # 4
