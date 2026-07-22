"""
Problem: Subarrays with K Different Integers
LeetCode #: 992
Difficulty: Hard
Link: https://leetcode.com/problems/subarrays-with-k-different-integers/

Approach: Exact K via At Most K. The number of subarrays with exactly K distinct integers equals `atMostK(nums, K) - atMostK(nums, K - 1)`. `atMostK` uses a standard sliding window to count subarrays with at most K distinct integers.
Time Complexity: O(N)
Space Complexity: O(N)
"""

from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(k_val: int) -> int:
            counts = defaultdict(int)
            left = 0
            res = 0

            for right in range(len(nums)):
                if counts[nums[right]] == 0:
                    k_val -= 1
                counts[nums[right]] += 1

                while k_val < 0:
                    counts[nums[left]] -= 1
                    if counts[nums[left]] == 0:
                        k_val += 1
                    left += 1

                res += right - left + 1

            return res

        return atMostK(k) - atMostK(k - 1)
