"""
Problem: 132 Pattern
LeetCode #: 456
Difficulty: Medium
Link: https://leetcode.com/problems/132-pattern/

Approach:
We need indices i < j < k such that nums[i] < nums[k] < nums[j].
Iterate backwards through `nums` while keeping track of the largest possible value for `nums[k]` (the '2' in '132').
Maintain a monotonic stack storing potential `nums[j]` values ('3').
For each element `nums[i]` ('1'):
- If `nums[i] < third` (where `third` represents `nums[k]`), we have found a valid 132 pattern!
- While stack has elements smaller than `nums[i]`, pop them and update `third` with popped value.
- Push `nums[i]` onto stack as a candidate for `nums[j]`.

Time Complexity: O(N) where N is length of nums array.
Space Complexity: O(N) for stack.
"""

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # Stores candidates for nums[j]
        third = float('-inf')  # Stores candidate for nums[k]

        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)

        return False
