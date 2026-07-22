"""
Problem: Sort Transformed Array
LeetCode #: 360
Difficulty: Medium
Link: https://leetcode.com/problems/sort-transformed-array/

Approach: Two Pointers on Parabola Extremes. Calculate f(x) = a*x^2 + b*x + c. Since the input is sorted, if a >= 0 the maximum values lie at the outer ends (left and right), so fill the result array from back to front. If a < 0, the minimum values lie at the outer ends, so fill from front to back.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def apply(x: int) -> int:
            return a * x * x + b * x + c

        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        idx = n - 1 if a >= 0 else 0

        while left <= right:
            val_left = apply(nums[left])
            val_right = apply(nums[right])

            if a >= 0:
                if val_left >= val_right:
                    res[idx] = val_left
                    left += 1
                else:
                    res[idx] = val_right
                    right -= 1
                idx -= 1
            else:
                if val_left <= val_right:
                    res[idx] = val_left
                    left += 1
                else:
                    res[idx] = val_right
                    right -= 1
                idx += 1

        return res
