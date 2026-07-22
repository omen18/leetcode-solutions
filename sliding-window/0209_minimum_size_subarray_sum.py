"""
Problem: Minimum Size Subarray Sum
LeetCode #: 209
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-size-subarray-sum/

Approach: Sliding Window (Two Pointers). Expand the right endpoint to add elements to the running sum. When the running sum reaches or exceeds `target`, update the minimum window length and shrink the left endpoint.
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        curr_sum = 0
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
