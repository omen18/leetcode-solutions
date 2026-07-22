"""
Problem: Find K-th Smallest Pair Distance
LeetCode #: 719
Difficulty: Hard
Link: https://leetcode.com/problems/find-k-th-smallest-pair-distance/

Approach: Sort nums. Binary search on distance `d` in range [0, nums[-1] - nums[0]]. Use two pointers to count number of pairs with distance <= d.
Time Complexity: O(n log n + n * log(max_diff))
Space Complexity: O(1) auxiliary space (or O(n) for sorting)
"""

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2

            # Two pointer count of pairs with distance <= mid
            count = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left
