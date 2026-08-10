"""
Problem: Contains Duplicate
LeetCode #: 217
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Approach: Use a hash set to track seen elements. If element exists in set, return True.
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# --- Test ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # False
