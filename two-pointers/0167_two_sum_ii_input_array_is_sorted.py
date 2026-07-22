"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode #: 167
Difficulty: Medium
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Approach: Two pointers starting at start (0) and end (n-1). Adjust pointers based on comparison of sum with target. 1-indexed output.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
