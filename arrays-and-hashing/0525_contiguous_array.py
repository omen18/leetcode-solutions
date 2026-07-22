"""
Problem: Contiguous Array
LeetCode #: 525
Difficulty: Medium
Link: https://leetcode.com/problems/contiguous-array/

Approach: Treat 0 as -1 and find longest subarray with sum 0 using prefix sum index map.
Time Complexity: O(N) where N is length of nums.
Space Complexity: O(N) for hash map storing prefix sum first-seen indices.
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        max_len = 0
        curr_count = 0

        for i, num in enumerate(nums):
            curr_count += 1 if num == 1 else -1
            if curr_count in seen:
                max_len = max(max_len, i - seen[curr_count])
            else:
                seen[curr_count] = i

        return max_len
