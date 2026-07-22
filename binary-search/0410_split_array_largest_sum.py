"""
Problem: Split Array Largest Sum
LeetCode #: 410
Difficulty: Hard
Link: https://leetcode.com/problems/split-array-largest-sum/

Approach: Binary search on the maximum subarray sum in range [max(nums), sum(nums)]. For a mid value, count how many subarrays are needed so no subarray sum exceeds mid.
Time Complexity: O(n * log(sum(nums) - max(nums)))
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) // 2
            count = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num

            if count <= k:
                right = mid
            else:
                left = mid + 1

        return left
