"""
Problem: Binary Search
LeetCode #: 704
Difficulty: Easy
Link: https://leetcode.com/problems/binary-search/

Approach: Classic binary search on sorted array.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))   # 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))    # -1
