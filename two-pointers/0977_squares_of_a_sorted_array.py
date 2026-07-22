"""
Problem: Squares of a Sorted Array
LeetCode #: 977
Difficulty: Easy
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Approach: Two Pointers from Ends. Place pointers at start (`left`) and end (`right`). Compare their squared values, place the larger squared value at the current end position of the result array, and shrink the corresponding pointer.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            sq_left = nums[left] * nums[left]
            sq_right = nums[right] * nums[right]

            if sq_left > sq_right:
                res[pos] = sq_left
                left += 1
            else:
                res[pos] = sq_right
                right -= 1
            pos -= 1

        return res
