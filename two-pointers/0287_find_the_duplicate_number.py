"""
Problem: Find the Duplicate Number
LeetCode #: 287
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/

Approach: Floyd's Cycle Detection (Tortoise and Hare). Treat the array as a linked list where `next(i) = nums[i]`. Find the intersection point of two pointers, then find the entrance to the cycle which corresponds to the duplicate number.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
