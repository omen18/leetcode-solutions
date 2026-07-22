"""
Problem: Best Time to Buy and Sell Stock III
LeetCode #: 123
Difficulty: Hard
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Approach: Dynamic Programming with state variables. Track 4 states:
- `buy1`: max profit after first buy (or minimum cost to buy first stock)
- `sell1`: max profit after first sell
- `buy2`: max profit after second buy
- `sell2`: max profit after second sell
Time Complexity: O(N)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2
