"""
Problem: Count Number of Nice Subarrays
LeetCode #: 1248
Difficulty: Medium
Link: https://leetcode.com/problems/count-number-of-nice-subarrays/

Approach: Convert problem to counting subarrays with `k` odd numbers. Exact count is `atMost(k) - atMost(k - 1)` using sliding window.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(goal: int) -> int:
            if goal < 0:
                return 0
            left = 0
            odds = 0
            count = 0
            for right in range(len(nums)):
                odds += nums[right] % 2
                while odds > goal:
                    odds -= nums[left] % 2
                    left += 1
                count += right - left + 1
            return count

        return atMost(k) - atMost(k - 1)
