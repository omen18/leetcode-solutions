"""
Problem: Best Time to Buy and Sell Stock with Transaction Fee
LeetCode #: 714
Difficulty: Medium
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Approach: Dynamic programming with state compression. Maintain `hold` (max profit holding a stock)
and `free` (max profit not holding a stock). For each day, update `hold` as max(hold, free - price)
and `free` as max(free, hold + price - fee).
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        free = 0
        hold = -prices[0]
        for price in prices[1:]:
            free = max(free, hold + price - fee)
            hold = max(hold, free - price)
        return free
