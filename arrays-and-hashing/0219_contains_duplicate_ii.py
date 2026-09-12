"""
Problem: Contains Duplicate II
LeetCode #: 219
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate-ii/

Approach: Hash map tracking most recent index of each number within window k.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # True
