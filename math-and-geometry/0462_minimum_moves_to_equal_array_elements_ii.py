"""
Problem: Minimum Moves to Equal Array Elements II
LeetCode #: 462
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

Approach: Find the median element after sorting and sum absolute differences.
Time Complexity: O(N log N)
Space Complexity: O(1) auxiliary
"""

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)
