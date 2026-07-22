"""
Problem: Maximum Points You Can Obtain from Cards
LeetCode #: 1423
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Approach: Taking `k` cards from either end is equivalent to leaving a contiguous subarray of length `n - k` with minimum sum. Use sliding window to find min sum subarray of size `n - k`.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k
        current_sum = sum(cardPoints[:window_size])
        min_window_sum = current_sum
        total_sum = sum(cardPoints)

        if window_size == 0:
            return total_sum

        for i in range(window_size, n):
            current_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_sum)

        return total_sum - min_window_sum
