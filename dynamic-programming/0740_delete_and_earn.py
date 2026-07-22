"""
Problem: Delete and Earn
LeetCode #: 740
Difficulty: Medium
Link: https://leetcode.com/problems/delete-and-earn/

Approach: Transform problem into House Robber. Sum up total points for each number value * count.
Since taking number `x` deletes `x - 1` and `x + 1`, we cannot pick adjacent number values. Use DP
with two variables `prev1` and `prev2` to track maximum points.
Time Complexity: O(N + M) where M is max value in nums
Space Complexity: O(M) for frequency buckets
"""

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        prev2 = 0
        prev1 = 0
        for p in points:
            curr = max(prev1, prev2 + p)
            prev2 = prev1
            prev1 = curr

        return prev1
