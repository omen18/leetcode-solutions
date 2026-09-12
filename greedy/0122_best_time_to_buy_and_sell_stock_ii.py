"""
Problem: Best Time to Buy and Sell Stock II
LeetCode #: 122
Difficulty: Medium
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Approach: Greedy approach: capture any positive price difference between consecutive days.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    print(sol.maxProfit([1, 2, 3, 4, 5]))     # 4
