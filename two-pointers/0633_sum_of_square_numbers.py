"""
Problem: Sum of Square Numbers
LeetCode #: 633
Difficulty: Medium
Link: https://leetcode.com/problems/sum-of-square-numbers/

Approach: Two pointers starting at `a = 0` and `b = int(math.isqrt(c))`. Calculate `a^2 + b^2` and adjust pointers inward until `a <= b`.
Time Complexity: O(sqrt(c))
Space Complexity: O(1)
"""

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, math.isqrt(c)

        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1

        return False
