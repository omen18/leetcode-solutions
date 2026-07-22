"""
Problem: Maximum Running Time of N Computers
LeetCode #: 2141
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-running-time-of-n-computers/

Approach: Binary search on runtime `t` in range [1, sum(batteries) // n]. A runtime `t` is achievable if sum(min(b, t) for b in batteries) >= n * t.
Time Complexity: O(m * log(sum(batteries) // n)) where m = len(batteries)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            total_power = sum(min(b, mid) for b in batteries)

            if total_power >= n * mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
