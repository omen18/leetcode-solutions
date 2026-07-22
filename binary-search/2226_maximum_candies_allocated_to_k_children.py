"""
Problem: Maximum Candies Allocated to K Children
LeetCode #: 2226
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

Approach: Binary search for maximum candy pile size in range [1, max(candies)]. Check if sum(c // mid for c in candies) >= k.
Time Complexity: O(n * log(max(candies)))
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        left, right = 1, max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)

            if count >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
